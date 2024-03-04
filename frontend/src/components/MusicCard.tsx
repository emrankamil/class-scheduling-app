import React from 'react';

interface PropData {
  owner: number;
  title: string;
  likes: number | null;
  stream: number | null;
  music_file: string;
  length: string | null;
  replays: number;
  music_cover_art: string;
}

const MusicCard: React.FC<PropData> = ({
  owner,
  title,
  likes,
  stream,
  music_file,
  length,
  replays,
  music_cover_art,
}) => {
  const playSong = () => {
    // Add logic to play the song here
    console.log('Playing the song:', music_file);
  };

  return (
    <div className="max-w-full bg-white shadow-md rounded-md overflow-hidden flex">
      <img
        src={music_cover_art}
        alt="Music Cover Art"
        className="w-1/3 h-48 object-cover"
      />
      <div className="w-2/3 p-4">
        <h3 className="text-xl font-semibold mb-2">{title}</h3>
        <p className="text-gray-600 mb-4">By Owner {owner}</p>
        <div className="flex items-center mb-4">
          {likes !== null && (
            <p className="mr-4">
              Likes: {likes} <i className="fas fa-thumbs-up"></i>
            </p>
          )}
          {stream !== null && (
            <p>
              Stream: {stream} <i className="fas fa-headphones"></i>
            </p>
          )}
        </div>
        {length !== null && <p className="text-gray-600 mb-4">Length: {length}</p>}
        <p className="text-gray-600 mb-4">Replays: {replays}</p>
        <button
          onClick={playSong}
          className="bg-blue-500 text-white px-4 py-2 rounded-md focus:outline-none"
        >
          Play Song
        </button>
      </div>
    </div>
  );
};

export default MusicCard;
