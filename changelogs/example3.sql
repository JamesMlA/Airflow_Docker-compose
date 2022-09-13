--liquibase formatted sql

--changeset anco:Create_Matches 
--comment: creando tabla
CREATE TABLE Matchesfds(	
MatchKey Serial PRIMARY KEY,	
MatchID INT NOT NULL,	
CategoryKey INT,	
ModelNumber varchar(50),	
Brand varchar(50),	
MatchTypeKey INT,	
CreatedDate  DATE  ,	
CreatedBy VARCHAR(10),	
deleatedDate Date,	
DeletedBy Varchar(10),	
StartDate Date,	
EndDate Date,	
Version int,	
CurrentFlag varchar(5)	
);	

