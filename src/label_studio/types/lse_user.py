# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["LseUser", "LseFields", "OrgMembership"]


class LseFields(BaseModel):
    invite_activated: Optional[bool] = None

    invite_expired: Optional[str] = None

    invite_expired_at: Optional[str] = None

    invited_at: Optional[datetime] = None

    invited_by: Optional[int] = None

    social_auth_finished: Optional[bool] = None
    """Is user finished social authentication"""

    trial_company: Optional[str] = None

    trial_experience_labeling: Optional[str] = None

    trial_license_enterprise: Optional[bool] = None

    trial_models_in_production: Optional[str] = None

    trial_role: Optional[
        Literal[
            "annotator",
            "annotator_team_manager",
            "business_analyst",
            "business_or_data_team_leadership",
            "data_engineer_platform_engineer",
            "data_scientist",
            "other",
        ]
    ] = None


class OrgMembership(BaseModel):
    role: str

    active: Optional[str] = None

    organization_id: Optional[str] = None


class LseUser(BaseModel):
    username: str

    id: Optional[int] = None

    active_organization: Optional[int] = None

    allow_newsletters: Optional[bool] = None
    """Allow sending newsletters to user"""

    avatar: Optional[str] = None

    email: Optional[str] = None

    first_name: Optional[str] = None

    initials: Optional[str] = None

    last_activity: Optional[datetime] = None

    last_name: Optional[str] = None

    lse_fields: Optional[LseFields] = None

    org_membership: Optional[List[OrgMembership]] = None

    password: Optional[str] = None

    phone: Optional[str] = None
