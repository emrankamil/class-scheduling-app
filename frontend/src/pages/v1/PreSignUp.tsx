import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const PreSignUp = () => {
  const navigate = useNavigate()
  const [userType, setUserType] = useState(null);

  const handleOptionSelect = (type:any) => {
    setUserType(type);
  };

  const handleSignup = () => {
    // Redirect to the respective signup page based on the selected user type
    if (userType === 'user') {
      navigate('/signup/user', {state:{'state':'user'}});
    } else if (userType === 'creator') {
      navigate('/signup/creator', {state:{'state':'user'}});
    }
  };

  return (
    <div className="container w-1/2 mx-auto mt-8">
      <h2 className="text-2xl font-semibold mb-4">Sign Up</h2>
      
      <div className="mb-4">
        <label className="block text-sm font-medium text-gray-600 mb-2">
          Join as a user or a Creator:
        </label>

        <div className="flex">
          <div className="mr-4 w-64 h-64 border-2">
            <input
              type="radio"
              id="userOption"
              name="userType"
              value="user"
              onChange={() => handleOptionSelect('user')}
            />
            <label htmlFor="userOption" className="ml-2">
              I am a user
            </label>
          </div>

          <div className='w-64 h-64 border-2'>
            <input
              type="radio"
              id="creatorOption"
              name="userType"
              value="creator"
              onChange={() => handleOptionSelect('creator')}
            />
            <label htmlFor="creatorOption" className="ml-2">
              I am a creator
            </label>
          </div>
        </div>
      </div>

      <button
        type="button"
        onClick={handleSignup}
        disabled={!userType} // Disable the button if userType is not selected
        className={`bg-blue-500 text-white px-4 py-2 rounded-md ${!userType && 'opacity-50 cursor-not-allowed'}`}
      >
        Sign Up
      </button>
    </div>
  );
};

export default PreSignUp;
