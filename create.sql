create table if not exists Genres (
	Genre_ID SERIAL primary key, 
	name VARCHAR(40) not null
);

create table if not exists Artists (
	Artist_ID SERIAL primary key, 
	name VARCHAR(60) not null
);

create table if not exists Artists_genres (
	artist_ID INTEGER not null references Artists(Artist_ID),
	genre_ID INTEGER not null references Genres(Genre_ID),
	constraint pk primary key (artist_ID, genre_ID)
);

create table if not exists Albums (
	Album_ID SERIAL primary key,
	name VARCHAR(100) not null,
	Release_year integer not null
);

create table if not exists Albums_artists (
	album_ID INTEGER not null references Albums(Album_ID),
	artist_ID INTEGER not null references Artists(Artist_ID),
	constraint ak primary key (album_ID, artist_ID)
);

create table if not exists Tracks (
	Track_ID SERIAL primary key,
	name VARCHAR(100) not null,
	Duration integer not null,
	album_ID INTEGER not null references Albums(Album_ID)
);

create table if not exists Collections (
	Collection_ID SERIAL primary key,
	name VARCHAR(100) not null,
	Release_year integer not null
);

create table if not exists Collections_tracks (
	track_ID INTEGER not null references Tracks(Track_ID),
	collection_ID INTEGER not null references Collections(Collection_ID),
	constraint sk primary key (track_ID, collection_ID)
);