"""initial migration

Revision ID: 24319a944774
Revises: 
Create Date: 2022-01-18 08:22:46.411802

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24319a944774'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('amounts',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('uuid', sa.String(length=50), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('last_modified', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('amount', sa.DECIMAL(precision=14, scale=2), server_default='0.00', nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('uuid')
    )
    op.create_index(op.f('ix_amounts_created_at'), 'amounts', ['created_at'], unique=False)
    op.create_table('groups',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('uuid', sa.String(length=50), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('last_modified', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('uuid')
    )
    op.create_index(op.f('ix_groups_created_at'), 'groups', ['created_at'], unique=False)
    op.create_table('guarantors',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('uuid', sa.String(length=50), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('last_modified', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('firstname', sa.String(length=45), nullable=False),
    sa.Column('lastname', sa.String(length=45), nullable=False),
    sa.Column('middlename', sa.String(length=45), nullable=True),
    sa.Column('phone', sa.String(length=20), nullable=False),
    sa.Column('address', sa.String(length=255), nullable=False),
    sa.Column('image', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('uuid')
    )
    op.create_index(op.f('ix_guarantors_created_at'), 'guarantors', ['created_at'], unique=False)
    op.create_table('loanpaymentstakeholders',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('uuid', sa.String(length=50), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('last_modified', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('uuid')
    )
    op.create_index(op.f('ix_loanpaymentstakeholders_created_at'), 'loanpaymentstakeholders', ['created_at'], unique=False)
    op.create_table('loantypes',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('uuid', sa.String(length=50), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('last_modified', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('min_payment_amount', sa.DECIMAL(precision=14, scale=2), nullable=False),
    sa.Column('total_loan_amount', sa.DECIMAL(precision=14, scale=2), nullable=False),
    sa.Column('loan_payment_cycle', sa.Integer(), nullable=False),
    sa.Column('loan_payment_duration', sa.Integer(), nullable=False),
    sa.Column('min_num_of_beneficiaries', sa.Integer(), server_default='1', nullable=False),
    sa.Column('max_num_of_beneficiaries', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('uuid')
    )
    op.create_index(op.f('ix_loantypes_created_at'), 'loantypes', ['created_at'], unique=False)
    op.create_table('localgovernments',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('uuid', sa.String(length=50), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('last_modified', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('display_name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('uuid')
    )
    op.create_index(op.f('ix_localgovernments_created_at'), 'localgovernments', ['created_at'], unique=False)
    op.create_index(op.f('ix_localgovernments_name'), 'localgovernments', ['name'], unique=True)
    op.create_table('nextofkins',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('uuid', sa.String(length=50), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('last_modified', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('firstname', sa.String(length=45), nullable=False),
    sa.Column('lastname', sa.String(length=45), nullable=False),
    sa.Column('middlename', sa.String(length=45), nullable=True),
    sa.Column('phone', sa.String(length=20), nullable=False),
    sa.Column('address', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('uuid')
    )
    op.create_index(op.f('ix_nextofkins_created_at'), 'nextofkins', ['created_at'], unique=False)
    op.create_table('passwordresets',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('uuid', sa.String(length=50), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('last_modified', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('expires', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('uuid')
    )
    op.create_index(op.f('ix_passwordresets_created_at'), 'passwordresets', ['created_at'], unique=False)
    op.create_table('permissions',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('uuid', sa.String(length=50), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('last_modified', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('uuid')
    )
    op.create_index(op.f('ix_permissions_created_at'), 'permissions', ['created_at'], unique=False)
    op.create_table('roles',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('uuid', sa.String(length=50), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('last_modified', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('uuid')
    )
    op.create_index(op.f('ix_roles_created_at'), 'roles', ['created_at'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('uuid', sa.String(length=50), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('last_modified', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('password_hash', sa.String(length=255), nullable=False),
    sa.Column('old_password_hash', sa.String(length=255), nullable=True),
    sa.Column('firstname', sa.String(length=255), nullable=True),
    sa.Column('lastname', sa.String(length=255), nullable=True),
    sa.Column('middlename', sa.String(length=255), nullable=True),
    sa.Column('phone', sa.String(length=50), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('is_system_user', sa.Boolean(), server_default='0', nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('uuid')
    )
    op.create_index(op.f('ix_users_created_at'), 'users', ['created_at'], unique=False)
    op.create_table('loanactivations',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('uuid', sa.String(length=50), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('last_modified', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('loaned_item_id', sa.String(length=100), nullable=False),
    sa.Column('activation_date', sa.Date(), nullable=False),
    sa.Column('effective_date', sa.Date(), nullable=False),
    sa.Column('performed_by', sa.String(length=100), nullable=False),
    sa.ForeignKeyConstraint(['performed_by'], ['users.uuid'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('uuid')
    )
    op.create_index(op.f('ix_loanactivations_created_at'), 'loanactivations', ['created_at'], unique=False)
    op.create_table('loandeactivations',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('uuid', sa.String(length=50), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('last_modified', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('loaned_item_id', sa.String(length=100), nullable=False),
    sa.Column('deactivation_date', sa.Date(), nullable=False),
    sa.Column('days_owing', sa.Integer(), nullable=False),
    sa.Column('days_paid_ahead', sa.Integer(), nullable=False),
    sa.Column('performed_by', sa.String(length=100), nullable=False),
    sa.ForeignKeyConstraint(['performed_by'], ['users.uuid'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('uuid')
    )
    op.create_index(op.f('ix_loandeactivations_created_at'), 'loandeactivations', ['created_at'], unique=False)
    op.create_table('loanpaymentstakes',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('uuid', sa.String(length=50), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('last_modified', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('stake_holder', sa.String(length=100), nullable=False),
    sa.Column('stake_name', sa.String(length=100), nullable=False),
    sa.Column('stake_amount', sa.DECIMAL(precision=14, scale=2), server_default='0.00', nullable=False),
    sa.Column('loan_type_name', sa.String(length=100), nullable=False),
    sa.ForeignKeyConstraint(['loan_type_name'], ['loantypes.name'], ),
    sa.ForeignKeyConstraint(['stake_holder'], ['loanpaymentstakeholders.name'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('stake_name'),
    sa.UniqueConstraint('uuid')
    )
    op.create_index(op.f('ix_loanpaymentstakes_created_at'), 'loanpaymentstakes', ['created_at'], unique=False)
    op.create_table('nins',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('uuid', sa.String(length=50), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('last_modified', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('nin', sa.String(length=16), nullable=False),
    sa.Column('firstname', sa.String(length=45), nullable=False),
    sa.Column('middlename', sa.String(length=45), nullable=False),
    sa.Column('lastname', sa.String(length=45), nullable=False),
    sa.Column('address', sa.String(length=160), nullable=False),
    sa.Column('phone', sa.String(length=16), nullable=False),
    sa.Column('gender', sa.Enum('m', 'f', 'na', name='gender_enum_1'), nullable=False),
    sa.Column('birthdate', sa.String(length=16), nullable=False),
    sa.Column('image', sa.String(length=160), nullable=False),
    sa.Column('pulled_by', sa.String(length=50), nullable=False),
    sa.Column('nin_type', sa.Enum('national', 'autogenerated', name='loan_nin_type_types'), server_default='national', nullable=False),
    sa.ForeignKeyConstraint(['pulled_by'], ['users.uuid'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nin'),
    sa.UniqueConstraint('uuid')
    )
    op.create_index(op.f('ix_nins_created_at'), 'nins', ['created_at'], unique=False)
    op.create_table('permission_role',
    sa.Column('permission_id', sa.String(length=50), nullable=True),
    sa.Column('role_id', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['permission_id'], ['permissions.uuid'], ),
    sa.ForeignKeyConstraint(['role_id'], ['roles.uuid'], )
    )
    op.create_table('role_group',
    sa.Column('role_id', sa.String(length=50), nullable=True),
    sa.Column('group_id', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['group_id'], ['groups.uuid'], ),
    sa.ForeignKeyConstraint(['role_id'], ['roles.uuid'], )
    )
    op.create_table('superwalletowners',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('uuid', sa.String(length=50), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('last_modified', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('display_name', sa.String(length=100), nullable=False),
    sa.Column('user_uuid', sa.String(length=50), nullable=False),
    sa.ForeignKeyConstraint(['user_uuid'], ['users.uuid'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('display_name'),
    sa.UniqueConstraint('user_uuid'),
    sa.UniqueConstraint('uuid')
    )
    op.create_index(op.f('ix_superwalletowners_created_at'), 'superwalletowners', ['created_at'], unique=False)
    op.create_table('units',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('uuid', sa.String(length=50), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('last_modified', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('unit_name', sa.String(length=50), nullable=False),
    sa.Column('unit_code', sa.String(length=50), nullable=False),
    sa.Column('local_government_uuid', sa.String(length=50), nullable=False),
    sa.Column('loan_type_uuid', sa.String(length=50), nullable=False),
    sa.ForeignKeyConstraint(['loan_type_uuid'], ['loantypes.uuid'], onupdate='CASCADE', ondelete='RESTRICT'),
    sa.ForeignKeyConstraint(['local_government_uuid'], ['localgovernments.uuid'], onupdate='CASCADE', ondelete='RESTRICT'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('unit_code'),
    sa.UniqueConstraint('unit_name'),
    sa.UniqueConstraint('uuid')
    )
    op.create_index(op.f('ix_units_created_at'), 'units', ['created_at'], unique=False)
    op.create_table('user_group',
    sa.Column('group_id', sa.String(length=50), nullable=True),
    sa.Column('user_id', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['group_id'], ['groups.uuid'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.uuid'], )
    )
    op.create_table('subunits',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('uuid', sa.String(length=50), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('last_modified', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('display_name', sa.String(length=50), nullable=True),
    sa.Column('unit_uuid', sa.String(length=50), nullable=False),
    sa.ForeignKeyConstraint(['unit_uuid'], ['units.uuid'], onupdate='CASCADE', ondelete='RESTRICT'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('uuid')
    )
    op.create_index(op.f('ix_subunits_created_at'), 'subunits', ['created_at'], unique=False)
    op.create_table('useraccounts',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('uuid', sa.String(length=50), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('last_modified', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('user_uuid', sa.String(length=50), nullable=False),
    sa.Column('nin', sa.String(length=16), nullable=True),
    sa.Column('image', sa.String(length=255), nullable=False),
    sa.Column('phone', sa.String(length=20), nullable=False),
    sa.Column('address', sa.String(length=255), nullable=False),
    sa.Column('gender', sa.Enum('m', 'f', 'na', name='gender_type_2'), nullable=False),
    sa.Column('birthdate', sa.Date(), nullable=False),
    sa.Column('next_of_kin_uuid', sa.String(length=50), nullable=True),
    sa.Column('creator_uuid', sa.String(length=50), nullable=False),
    sa.ForeignKeyConstraint(['creator_uuid'], ['users.uuid'], ),
    sa.ForeignKeyConstraint(['next_of_kin_uuid'], ['nextofkins.uuid'], ),
    sa.ForeignKeyConstraint(['nin'], ['nins.nin'], ),
    sa.ForeignKeyConstraint(['user_uuid'], ['users.uuid'], onupdate='CASCADE', ondelete='RESTRICT'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nin'),
    sa.UniqueConstraint('uuid')
    )
    op.create_index(op.f('ix_useraccounts_created_at'), 'useraccounts', ['created_at'], unique=False)
    op.create_table('wallets',
    sa.Column('wallet_number', sa.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('owner_uuid', sa.String(length=45), nullable=False),
    sa.Column('super_wallet_owner_uuid', sa.String(length=45), nullable=True),
    sa.Column('balance', sa.DECIMAL(precision=18, scale=2), server_default='0.00', nullable=False),
    sa.Column('status', sa.Enum('enabled', 'disabled', 'closed', name='wallet_status_type'), server_default='enabled', nullable=False),
    sa.Column('uuid', sa.String(length=50), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('last_modified', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['owner_uuid'], ['users.uuid'], ),
    sa.ForeignKeyConstraint(['super_wallet_owner_uuid'], ['superwalletowners.uuid'], ),
    sa.PrimaryKeyConstraint('wallet_number'),
    sa.UniqueConstraint('owner_uuid'),
    sa.UniqueConstraint('uuid'),
    mysql_auto_increment='4136000001'
    )
    op.create_index(op.f('ix_wallets_created_at'), 'wallets', ['created_at'], unique=False)
    op.create_table('loanpaymentaccounts',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('uuid', sa.String(length=50), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('last_modified', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('loan_payer_uuid', sa.String(length=100), nullable=False),
    sa.Column('loaned_item_id', sa.String(length=100), nullable=False),
    sa.Column('loan_type_uuid', sa.String(length=100), nullable=False),
    sa.Column('paid_till_date', sa.Date(), nullable=False),
    sa.Column('status', sa.Enum('activated', 'deactivated', 'blacklisted', name='loan_payment_account_status_type'), server_default='activated', nullable=False),
    sa.ForeignKeyConstraint(['loan_payer_uuid'], ['useraccounts.uuid'], ),
    sa.ForeignKeyConstraint(['loan_type_uuid'], ['loantypes.uuid'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('loaned_item_id'),
    sa.UniqueConstraint('uuid')
    )
    op.create_index(op.f('ix_loanpaymentaccounts_created_at'), 'loanpaymentaccounts', ['created_at'], unique=False)
    op.create_table('vehicles',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('uuid', sa.String(length=50), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('last_modified', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('vehicle_type_uuid', sa.String(length=50), nullable=False),
    sa.Column('chassis_number', sa.String(length=50), nullable=False),
    sa.Column('engine_number', sa.String(length=50), nullable=False),
    sa.Column('tracking_id', sa.String(length=50), nullable=True),
    sa.Column('vehicle_id', sa.String(length=45), nullable=False),
    sa.Column('vehicle_subunit_uuid', sa.String(length=50), nullable=False),
    sa.Column('registration_date', sa.Date(), nullable=False),
    sa.Column('unique_key', sa.String(length=50), nullable=False),
    sa.Column('creator_uuid', sa.String(length=50), nullable=False),
    sa.Column('qr_code_image', sa.String(length=255), nullable=False),
    sa.Column('status', sa.Enum('not_activated', 'activated', 'deactivated', 'blacklisted', name='vehicle_status_type'), nullable=False),
    sa.ForeignKeyConstraint(['creator_uuid'], ['users.uuid'], ),
    sa.ForeignKeyConstraint(['vehicle_subunit_uuid'], ['subunits.uuid'], onupdate='CASCADE', ondelete='RESTRICT'),
    sa.ForeignKeyConstraint(['vehicle_type_uuid'], ['loantypes.uuid'], onupdate='CASCADE', ondelete='RESTRICT'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('chassis_number'),
    sa.UniqueConstraint('engine_number'),
    sa.UniqueConstraint('tracking_id'),
    sa.UniqueConstraint('unique_key'),
    sa.UniqueConstraint('uuid'),
    sa.UniqueConstraint('vehicle_id')
    )
    op.create_index(op.f('ix_vehicles_created_at'), 'vehicles', ['created_at'], unique=False)
    op.create_table('wallettransactions',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('uuid', sa.String(length=50), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('last_modified', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('wallet_number', sa.BIGINT(), nullable=False),
    sa.Column('type', sa.Enum('credit', 'debit', name='wallet_txn_status_type'), server_default='credit', nullable=False),
    sa.Column('amount', sa.DECIMAL(precision=18, scale=2), server_default='0.00', nullable=False),
    sa.Column('performed_by', sa.String(length=50), nullable=False),
    sa.ForeignKeyConstraint(['performed_by'], ['users.uuid'], ),
    sa.ForeignKeyConstraint(['wallet_number'], ['wallets.wallet_number'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('uuid')
    )
    op.create_index(op.f('ix_wallettransactions_created_at'), 'wallettransactions', ['created_at'], unique=False)
    op.create_table('loanpaymenttxns',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('uuid', sa.String(length=50), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('last_modified', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('loaned_item_id', sa.String(length=100), nullable=False),
    sa.Column('amount', sa.DECIMAL(precision=14, scale=2), server_default='0.00', nullable=False),
    sa.Column('days_paid', sa.Integer(), nullable=False),
    sa.Column('txn_id', sa.String(length=100), nullable=False),
    sa.Column('txn_receipt', sa.String(length=100), nullable=False),
    sa.Column('wallet_txn_uuid', sa.String(length=45), nullable=False),
    sa.Column('loan_type_uuid', sa.String(length=45), nullable=False),
    sa.Column('txn_date', sa.Date(), nullable=False),
    sa.Column('performed_by', sa.String(length=100), nullable=False),
    sa.ForeignKeyConstraint(['loan_type_uuid'], ['loantypes.uuid'], ),
    sa.ForeignKeyConstraint(['loaned_item_id'], ['loanpaymentaccounts.loaned_item_id'], ),
    sa.ForeignKeyConstraint(['performed_by'], ['users.uuid'], ),
    sa.ForeignKeyConstraint(['wallet_txn_uuid'], ['wallettransactions.uuid'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('txn_id'),
    sa.UniqueConstraint('uuid')
    )
    op.create_index(op.f('ix_loanpaymenttxns_created_at'), 'loanpaymenttxns', ['created_at'], unique=False)
    op.create_table('loanpaymentbreakdowns',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('uuid', sa.String(length=50), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('last_modified', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('stake_holder', sa.String(length=100), nullable=False),
    sa.Column('stake_name', sa.String(length=100), nullable=False),
    sa.Column('amount', sa.DECIMAL(precision=14, scale=2), server_default='0.00', nullable=False),
    sa.Column('loan_payment_txn_uuid', sa.String(length=45), nullable=False),
    sa.Column('txn_date', sa.Date(), nullable=False),
    sa.Column('performed_by', sa.String(length=100), nullable=False),
    sa.ForeignKeyConstraint(['loan_payment_txn_uuid'], ['loanpaymenttxns.uuid'], ),
    sa.ForeignKeyConstraint(['performed_by'], ['users.uuid'], ),
    sa.ForeignKeyConstraint(['stake_holder'], ['loanpaymentstakeholders.name'], ),
    sa.ForeignKeyConstraint(['stake_name'], ['loanpaymentstakes.stake_name'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('uuid')
    )
    op.create_index(op.f('ix_loanpaymentbreakdowns_created_at'), 'loanpaymentbreakdowns', ['created_at'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_loanpaymentbreakdowns_created_at'), table_name='loanpaymentbreakdowns')
    op.drop_table('loanpaymentbreakdowns')
    op.drop_index(op.f('ix_loanpaymenttxns_created_at'), table_name='loanpaymenttxns')
    op.drop_table('loanpaymenttxns')
    op.drop_index(op.f('ix_wallettransactions_created_at'), table_name='wallettransactions')
    op.drop_table('wallettransactions')
    op.drop_index(op.f('ix_vehicles_created_at'), table_name='vehicles')
    op.drop_table('vehicles')
    op.drop_index(op.f('ix_loanpaymentaccounts_created_at'), table_name='loanpaymentaccounts')
    op.drop_table('loanpaymentaccounts')
    op.drop_index(op.f('ix_wallets_created_at'), table_name='wallets')
    op.drop_table('wallets')
    op.drop_index(op.f('ix_useraccounts_created_at'), table_name='useraccounts')
    op.drop_table('useraccounts')
    op.drop_index(op.f('ix_subunits_created_at'), table_name='subunits')
    op.drop_table('subunits')
    op.drop_table('user_group')
    op.drop_index(op.f('ix_units_created_at'), table_name='units')
    op.drop_table('units')
    op.drop_index(op.f('ix_superwalletowners_created_at'), table_name='superwalletowners')
    op.drop_table('superwalletowners')
    op.drop_table('role_group')
    op.drop_table('permission_role')
    op.drop_index(op.f('ix_nins_created_at'), table_name='nins')
    op.drop_table('nins')
    op.drop_index(op.f('ix_loanpaymentstakes_created_at'), table_name='loanpaymentstakes')
    op.drop_table('loanpaymentstakes')
    op.drop_index(op.f('ix_loandeactivations_created_at'), table_name='loandeactivations')
    op.drop_table('loandeactivations')
    op.drop_index(op.f('ix_loanactivations_created_at'), table_name='loanactivations')
    op.drop_table('loanactivations')
    op.drop_index(op.f('ix_users_created_at'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_roles_created_at'), table_name='roles')
    op.drop_table('roles')
    op.drop_index(op.f('ix_permissions_created_at'), table_name='permissions')
    op.drop_table('permissions')
    op.drop_index(op.f('ix_passwordresets_created_at'), table_name='passwordresets')
    op.drop_table('passwordresets')
    op.drop_index(op.f('ix_nextofkins_created_at'), table_name='nextofkins')
    op.drop_table('nextofkins')
    op.drop_index(op.f('ix_localgovernments_name'), table_name='localgovernments')
    op.drop_index(op.f('ix_localgovernments_created_at'), table_name='localgovernments')
    op.drop_table('localgovernments')
    op.drop_index(op.f('ix_loantypes_created_at'), table_name='loantypes')
    op.drop_table('loantypes')
    op.drop_index(op.f('ix_loanpaymentstakeholders_created_at'), table_name='loanpaymentstakeholders')
    op.drop_table('loanpaymentstakeholders')
    op.drop_index(op.f('ix_guarantors_created_at'), table_name='guarantors')
    op.drop_table('guarantors')
    op.drop_index(op.f('ix_groups_created_at'), table_name='groups')
    op.drop_table('groups')
    op.drop_index(op.f('ix_amounts_created_at'), table_name='amounts')
    op.drop_table('amounts')
    # ### end Alembic commands ###
