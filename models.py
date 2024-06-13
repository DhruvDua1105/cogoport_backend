from sqlalchemy import Column, Integer, String
from app.database import Base

class CountryConfiguration(Base):
    """
    SQLAlchemy model for storing country configurations.

    Represents a table 'country_configurations' in the database.

    Attributes:
    - id (int): Primary key for the country configuration.
    - country_code (str): Country code of the country.
    - business_name (str): Business name associated with the country configuration.
    - registration_number (str): Registration number related to the country configuration.
    """
    __tablename__ = 'country_configurations'

    id = Column(Integer, primary_key=True, index=True)
    country_code = Column(String, unique=True, index=True, nullable=False)
    business_name = Column(String, nullable=False)
    registration_number = Column(String, nullable=True)
    additional_details = Column(String, nullable=True)
    # Add other necessary fields
