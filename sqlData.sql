CREATE TABLE IF NOT EXISTS SocialMediaPosts (
    id INTEGER PRIMARY KEY ,
    category TEXT,
    post_date DATETIME,
    post_title TEXT,
    post_topic TEXT,
    post_content TEXT,
    likes INTEGER,
    comments INTEGER,
    shares INTEGER,
    hashtags TEXT,
    keywords TEXT,
    source_url TEXT,
    click_through_rate REAL,
    time_spent INTEGER,
    bounce_rate REAL,
    location_name TEXT
);



CREATE TABLE IF NOT EXISTS NewsArticles (
    id INTEGER PRIMARY KEY ,
    category TEXT,
    article_date DATETIME,
    article_title TEXT,
    article_topic TEXT,
    article_content TEXT,
    sentiment DECIMAL,
    likes INTEGER,
    comments INTEGER,
    shares INTEGER,
    keywords TEXT,
    hashtags TEXT,
    source_url TEXT,
    tags TEXT,
    click_through_rate REAL,
    time_spent INTEGER,
    bounce_rate REAL,
    location_name TEXT
);

