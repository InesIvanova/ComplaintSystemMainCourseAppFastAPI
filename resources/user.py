from typing import Optional, List

from fastapi import APIRouter, Depends

from managers.auth import oauth2_scheme, is_admin
from managers.user import UserManager
from models import RoleType
from schemas.response.user import UserOut

router = APIRouter(tags=["Users"])


@router.get(
    "/users/",
    dependencies=[Depends(oauth2_scheme), Depends(is_admin)],
    response_model=List[UserOut],
)
async def get_users(email: Optional[str] = None):
    if email:
        return await UserManager.get_user_by_email(email)
    return await UserManager.get_all_users()


@router.put(
    "/users/{user_id}/make-admin",
    dependencies=[Depends(oauth2_scheme), Depends(is_admin)],
    status_code=204,
)
async def make_admin(user_id: int):
    await UserManager.change_role(RoleType.admin, user_id)


@router.put(
    "/users/{user_id}/make-approver",
    dependencies=[Depends(oauth2_scheme), Depends(is_admin)],
    status_code=204,
)
async def make_approver(user_id: int):
    await UserManager.change_role(RoleType.approver, user_id)
