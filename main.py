from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import app.models as models
import app.schemas as schemas
from app.database import engine, SessionLocal
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create all database tables based on the models
models.Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/create_configuration", response_model=schemas.CountryConfiguration)
def create_configuration(config: schemas.CountryConfigurationCreate, db: Session = Depends(get_db)):
    """
    Create a new country configuration.

    Parameters:
    - config: schema containing country configuration details

    Returns:
    - Newly created country configuration
    """
    db_config = models.CountryConfiguration(
        country_code=config.country_code,
        business_name=config.business_name,
        registration_number=config.registration_number,
        additional_details=config.additional_details  # Ensure this field is included
    )
    db.add(db_config)
    db.commit()
    db.refresh(db_config)
    
    logger.info(f"Created configuration for country_code: {config.country_code}")
    
    # Return the newly created configuration
    return db_config

@app.get("/get_configuration/{country_code}", response_model=schemas.CountryConfiguration)
def get_configuration(country_code: str, db: Session = Depends(get_db)):
    """
    Get country configuration by country code.

    Parameters:
    - country_code: code of the country to retrieve configuration for

    Returns:
    - Country configuration details if found
    """
    config = db.query(models.CountryConfiguration).filter(models.CountryConfiguration.country_code == country_code).first()
    if config is None:
        # Return HTTP 404 Not Found if configuration not found
        raise HTTPException(status_code=404, detail="Country configuration not found")
    
    logger.info(f"Retrieved configuration for country_code: {country_code}")
    
    # Return the found configuration
    return config

@app.post("/update_configuration", response_model=schemas.CountryConfiguration)
def update_configuration(config: schemas.CountryConfigurationUpdate, db: Session = Depends(get_db)):
    """
    Update country configuration.

    Parameters:
    - config: schema containing updated country configuration details

    Returns:
    - Updated country configuration
    """
    db_config = db.query(models.CountryConfiguration).filter(models.CountryConfiguration.country_code == config.country_code).first()
    if db_config:
        # Update fields based on the provided schema
        db_config.business_name = config.business_name
        db_config.registration_number = config.registration_number
        db.commit()
        db.refresh(db_config)
        
        logger.info(f"Updated configuration for country_code: {config.country_code}")
        
        # Return the updated configuration
        return db_config
    else:
        # Return HTTP 404 Not Found if configuration not found
        raise HTTPException(status_code=404, detail="Country configuration not found")

@app.delete("/delete_configuration", response_model=dict)
def delete_configuration(country_code: str, db: Session = Depends(get_db)):
    """
    Delete country configuration.

    Parameters:
    - country_code: code of the country configuration to delete

    Returns:
    - Message indicating success or failure
    """
    db_config = db.query(models.CountryConfiguration).filter(models.CountryConfiguration.country_code == country_code).first()
    if db_config:
        db.delete(db_config)
        db.commit()
        
        logger.info(f"Deleted configuration for country_code: {country_code}")
        
        # Return success message
        return {"message": f"Country configuration for {country_code} deleted successfully"}
    else:
        # Return HTTP 404 Not Found if configuration not found
        raise HTTPException(status_code=404, detail="Country configuration not found")
