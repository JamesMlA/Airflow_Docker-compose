--liquibase formatted sql

--changeset anco:1 labels:1.0
--comment: some comment
CREATE TABLE ProductMatche345(		
MatchID INT NOT NULL,		
ProductID INT NOT NULL,		
deleatedDate Date,		
DeletedBy Varchar(10),		
CreatedDate DATE ,		
CreatedBy VARCHAR(10)		
);