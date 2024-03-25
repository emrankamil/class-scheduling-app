import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const Landing = () => {
  const navigate = useNavigate()
  const [version, setVersion] = useState(null);

  const handleOptionSelect = (type:any) => {
    setVersion(type);
  };

  const handleContinue = () => {
    if (version === 'v1') {
      navigate('/v1', {state:{'state':'v1'}});
    } else if (version === 'v2') {
      navigate('/v2', {state:{'state':'v2'}});
    }
  };

  return (
    <div className="flex flex-col items-center mt-8">
      <div className="flex space-x-4">
        <button
          className={`${
            version === 'v1'
              ? 'bg-blue-500 text-white'
              : 'bg-gray-300 text-gray-700'
          } py-2 px-4 rounded w-40 h-40`}
          onClick={() => handleOptionSelect('v1')}
        >
          V1
        </button>
        <button
          className={`${
            version === 'v2'
              ? 'bg-blue-500 text-white'
              : 'bg-gray-300 text-gray-700'
          } py-2 px-4 rounded w-40 h-40`}
          onClick={() => handleOptionSelect('v2')}
        >
          V2
        </button>
      </div>
      <button
        type='button'
        className={`${
          version ? 'bg-blue-500 hover:bg-blue-700' : 'bg-gray-300'
        } text-white py-2 px-4 mt-4 rounded`}
        onClick={handleContinue}
        disabled={!version}
      >
        Get Started
      </button>
    </div>
  );
};

export default Landing;
