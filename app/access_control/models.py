from sqlalchemy import Column, ForeignKey, Integer, Table
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import String

from app.config.database import Base
from app.mixins.columns import BaseMixin, BaseUACMixin



# Many to Many associations
permission_role = Table('permission_role', Base.metadata,
    Column('permission_id', String(length=50), ForeignKey('permissions.uuid')),
    Column('role_id', String(length=50), ForeignKey('roles.uuid'))
)
role_group = Table('role_group', Base.metadata,
    Column('role_id', String(length=50), ForeignKey('roles.uuid')),
    Column('group_id', String(length=50), ForeignKey('groups.uuid'))
)


class Permission(BaseUACMixin, Base):
    pass


class Role(BaseUACMixin, Base):
    permissions: relationship = relationship("Permission", secondary=permission_role)


class Group(BaseUACMixin, Base):
    roles: relationship = relationship("Role", secondary=role_group)