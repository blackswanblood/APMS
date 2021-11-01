CREATE TABLE Gift_1 (
    ID INTEGER PRIMARY KEY,
    Category CHAR(30) NOT NULL,
    FOREIGN KEY (Category) REFERENCES Gift_2
);

CREATE TABLE Gift_2 (
    Category CHAR(30) PRIMARY KEY, 
    PointsRequired INTEGER NOT NULL
);

CREATE TABLE Tourist (
    ID INTEGER PRIMARY KEY, 
    Name CHAR(30) NOT NULL, 
    Age INTEGER, 
    ArcadePoints INTEGER
);

CREATE TABLE TouristBuysTicket (
    TID INTEGER, 
    TicketNo INTEGER,
    PRIMARY KEY (TID, TicketNo),
    FOREIGN KEY (TID) REFERENCES Tourist(ID), 
    FOREIGN KEY (TicketNo) REFERENCES Ticket_1
);

CREATE TABLE Redeems (
    GID INTEGER, 
    TID INTEGER,
    PRIMARY KEY (GID, TID), 
    FOREIGN KEY (GID) REFERENCES Gift_1(ID), 
    FOREIGN KEY (TID) REFERENCES Tourist(ID)
);

CREATE TABLE Ticket_1 (
    TicketNo INTEGER PRIMARY KEY, 
    Type CHAR(30) NOT NULL,
    FOREIGN KEY (Type) REFERENCES Ticket_2
);

CREATE TABLE Ticket_2 (
    Type CHAR(30) PRIMARY KEY, 
    Price INTEGER NOT NULL
);

CREATE TABLE TicketForRide (
    TicketNo INTEGER, 
    RideName CHAR(50),
    PRIMARY KEY (TicketNo, RideName),
    FOREIGN KEY (TicketNo) REFERENCES Ticket_1,
    FOREIGN KEY (RideName) REFERENCES Ride_Maintains(RName)
);

CREATE TABLE Arcade (
    Name CHAR(30) PRIMARY KEY, 
    Location CHAR(50),
    UNIQUE (Location)
);

CREATE TABLE ArcadeHasGift (
    AName CHAR(30),
    GID INTEGER,
    PRIMARY KEY (AName, GID),
    FOREIGN KEY (AName) REFERENCES Arcade(Name),
    FOREIGN KEY (GID) REFERENCES Gift_1(ID)
);

CREATE TABLE Machine (
    AName CHAR(30), 
    MName CHAR(30), 
    Type CHAR(30), 
    Highscores INTEGER,
    PRIMARY KEY (AName, MName),
    FOREIGN KEY (AName) REFERENCES Arcade(Name)
        ON DELETE CASCADE
);

CREATE TABLE TouristPlaysMachine (
    TID INTEGER, 
    AName CHAR(30), 
    MName CHAR(30), 
    PointsEarned INTEGER,
    PRIMARY KEY (TID, AName, MName),
    FOREIGN KEY (TID) REFERENCES Tourist(ID),
    FOREIGN KEY (AName, MName) REFERENCES Machine(AName, MName)
);


CREATE TABLE Staff (
    WorkID INTEGER PRIMARY KEY, 
    Name CHAR(30) NOT NULL
);

CREATE TABLE Cashier_WorksAt (
    WorkID INTEGER PRIMARY KEY, 
    AName CHAR(30) NOT NULL,
    FOREIGN KEY (WorkID) REFERENCES Staff
        ON DELETE CASCADE,
    FOREIGN KEY (AName) REFERENCES Arcade
        ON DELETE SET NULL 
);

CREATE TABLE Operator_Operates_1 (
    WorkID INTEGER PRIMARY KEY, 
    Qualification CHAR(50),
    FOREIGN KEY (WorkID) REFERENCES Staff(WorkID)
        ON DELETE CASCADE, 
    FOREIGN KEY (Qualification) REFERENCES Operator_Operates_2
);

CREATE TABLE Operator_Operates_2 (
    Qualification CHAR(50) PRIMARY KEY,
    RName CHAR(30),
    FOREIGN KEY (RName) REFERENCES Ride_Maintains(RName)
        ON DELETE SET NULL 
);

CREATE TABLE Technician (
    WorkID INTEGER PRIMARY KEY, 
    Qualification CHAR(50),
    FOREIGN KEY (WorkID) REFERENCES Staff(WorkID)
        ON DELETE CASCADE
);

CREATE TABLE Equipment (
    ID INTEGER PRIMARY KEY
);

CREATE TABLE Uses (
    WID INTEGER, 
    EID INTEGER,
    PRIMARY KEY (WID, EID),
    FOREIGN KEY (WID) references Technician(WorkID)
        ON DELETE CASCADE,
    FOREIGN KEY (EID) references Equipment(ID)
        ON DELETE CASCADE
);

CREATE TABLE Ride_Maintains (
    RName CHAR(30) PRIMARY KEY, 
    PassengerLimit INTEGER NOT NULL, 
    WorkID INTEGER NOT NULL, 
    EID INTEGER NOT NULL, 
    TimeofInspection DATE,
    FOREIGN KEY (WorkID) REFERENCES Technician(WorkID)
        ON DELETE SET NULL,
    FOREIGN KEY (EID) REFERENCES Equipment(ID)
        ON DELETE SET NULL
);


