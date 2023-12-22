"""Starting over with alembic

Revision ID: 9ca84d790c80
Revises: 
Create Date: 2023-12-22 10:15:27.997885

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '9ca84d790c80'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('hotels',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('contact_info', sa.String(), nullable=True),
    sa.Column('amenities', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.Column('policies', sa.String(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.Date(), nullable=False),
    sa.Column('updated_at', sa.Date(), nullable=False),
    sa.Column('is_deleted', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_hotels_id'), 'hotels', ['id'], unique=False)
    op.create_index(op.f('ix_hotels_name'), 'hotels', ['name'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('hashed_password', sa.String(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.create_table('booking_policies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('hotel_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('policy_text', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['hotel_id'], ['hotels.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_booking_policies_id'), 'booking_policies', ['id'], unique=False)
    op.create_index(op.f('ix_booking_policies_name'), 'booking_policies', ['name'], unique=False)
    op.create_table('meal_options',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('hotel_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['hotel_id'], ['hotels.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_meal_options_id'), 'meal_options', ['id'], unique=False)
    op.create_index(op.f('ix_meal_options_name'), 'meal_options', ['name'], unique=False)
    op.create_table('room_types',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('hotel_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('number_of_rooms', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['hotel_id'], ['hotels.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_room_types_id'), 'room_types', ['id'], unique=False)
    op.create_index(op.f('ix_room_types_name'), 'room_types', ['name'], unique=False)
    op.create_table('seasons',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('hotel_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('start_date', sa.Date(), nullable=True),
    sa.Column('end_date', sa.Date(), nullable=True),
    sa.Column('hotel_foc_slots', sa.String(), nullable=True),
    sa.Column('diving_foc_slots', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['hotel_id'], ['hotels.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_seasons_id'), 'seasons', ['id'], unique=False)
    op.create_index(op.f('ix_seasons_name'), 'seasons', ['name'], unique=False)
    op.create_table('special_offers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('hotel_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['hotel_id'], ['hotels.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_special_offers_id'), 'special_offers', ['id'], unique=False)
    op.create_index(op.f('ix_special_offers_name'), 'special_offers', ['name'], unique=False)
    op.create_table('user_preferences',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_preferences_id'), 'user_preferences', ['id'], unique=False)
    op.create_table('user_profiles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('phone_number', sa.String(), nullable=True),
    sa.Column('company_name', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_profiles_id'), 'user_profiles', ['id'], unique=False)
    op.create_table('diving_packages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('season_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['season_id'], ['seasons.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_diving_packages_id'), 'diving_packages', ['id'], unique=False)
    op.create_index(op.f('ix_diving_packages_name'), 'diving_packages', ['name'], unique=False)
    op.create_table('occupancy_rates',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('room_type_id', sa.Integer(), nullable=True),
    sa.Column('season_id', sa.Integer(), nullable=True),
    sa.Column('occupancy_type', sa.Enum('SINGLE', 'DOUBLE', 'TRIPLE', 'QUADRUPLE', name='occupancytype'), nullable=False),
    sa.Column('rate', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['room_type_id'], ['room_types.id'], ),
    sa.ForeignKeyConstraint(['season_id'], ['seasons.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_occupancy_rates_id'), 'occupancy_rates', ['id'], unique=False)
    op.create_table('group_contracts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('hotel_id', sa.Integer(), nullable=True),
    sa.Column('group_name', sa.String(), nullable=True),
    sa.Column('customer', sa.String(), nullable=True),
    sa.Column('start_date', sa.Date(), nullable=True),
    sa.Column('end_date', sa.Date(), nullable=True),
    sa.Column('travel_agent', sa.String(), nullable=True),
    sa.Column('contract', sa.String(), nullable=True),
    sa.Column('diving_package_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['diving_package_id'], ['diving_packages.id'], ),
    sa.ForeignKeyConstraint(['hotel_id'], ['hotels.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_group_contracts_group_name'), 'group_contracts', ['group_name'], unique=False)
    op.create_index(op.f('ix_group_contracts_id'), 'group_contracts', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_group_contracts_id'), table_name='group_contracts')
    op.drop_index(op.f('ix_group_contracts_group_name'), table_name='group_contracts')
    op.drop_table('group_contracts')
    op.drop_index(op.f('ix_occupancy_rates_id'), table_name='occupancy_rates')
    op.drop_table('occupancy_rates')
    op.drop_index(op.f('ix_diving_packages_name'), table_name='diving_packages')
    op.drop_index(op.f('ix_diving_packages_id'), table_name='diving_packages')
    op.drop_table('diving_packages')
    op.drop_index(op.f('ix_user_profiles_id'), table_name='user_profiles')
    op.drop_table('user_profiles')
    op.drop_index(op.f('ix_user_preferences_id'), table_name='user_preferences')
    op.drop_table('user_preferences')
    op.drop_index(op.f('ix_special_offers_name'), table_name='special_offers')
    op.drop_index(op.f('ix_special_offers_id'), table_name='special_offers')
    op.drop_table('special_offers')
    op.drop_index(op.f('ix_seasons_name'), table_name='seasons')
    op.drop_index(op.f('ix_seasons_id'), table_name='seasons')
    op.drop_table('seasons')
    op.drop_index(op.f('ix_room_types_name'), table_name='room_types')
    op.drop_index(op.f('ix_room_types_id'), table_name='room_types')
    op.drop_table('room_types')
    op.drop_index(op.f('ix_meal_options_name'), table_name='meal_options')
    op.drop_index(op.f('ix_meal_options_id'), table_name='meal_options')
    op.drop_table('meal_options')
    op.drop_index(op.f('ix_booking_policies_name'), table_name='booking_policies')
    op.drop_index(op.f('ix_booking_policies_id'), table_name='booking_policies')
    op.drop_table('booking_policies')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_hotels_name'), table_name='hotels')
    op.drop_index(op.f('ix_hotels_id'), table_name='hotels')
    op.drop_table('hotels')
    # ### end Alembic commands ###