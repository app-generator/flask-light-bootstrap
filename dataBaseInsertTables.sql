 CREATE TABLE IF NOT EXISTS users 
            (id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(20) NOT NULL,
            password VARCHAR(30) NOT NULL,
            email VARCHAR(40) NOT NULL, 
            activePremium BIT NOT NULL,
            BillingDate DATE  );

      
        
    CREATE TABLE IF NOT EXISTS newsArticles 
        (id INT AUTO_INCREMENT PRIMARY KEY,
        category	TEXT,
        date	DATETIME,
        title	TEXT,
        topic	TEXT,
        content	TEXT,
        sentiment	DECIMAL,
        likes	INTEGER,
        comments	INTEGER,
        shares	INTEGER,
        keywords	TEXT,
        hashtags	TEXT,
        source_url	TEXT,
        tags	TEXT,
        ctr	REAL,
        spent	INTEGER,
        bounce_rate	REAL,
        location_name	TEXT  );
       
     