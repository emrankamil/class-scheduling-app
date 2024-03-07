import React from 'react';

const Dropdown = ({ editMode, value, options, onChange }) => {
  return editMode ? (
    <div className="relative">
      <select
        className={`appearance-none block w-full bg-white text-gray-700 border rounded py-3 px-4 m-1 focus:outline-gray leading-tight`}
        value={value}
        onChange={(e) => onChange(e)}
      >
        {options.map((option, index) => (
          <option key={index} value={option}>
            {option}
          </option>
        ))}
      </select>
      <div className="absolute inset-y-0 right-0 flex items-center px-2 pointer-events-none">
        <svg className="w-4 h-4 fill-current text-gray-700" viewBox="0 0 20 20">
          <path
            d="M10 12l-6-6-1.414 1.414L10 14.828l7.414-7.414L16 6z"
            clipRule="evenodd"
            fillRule="evenodd"
          />
        </svg>
      </div>
    </div>
  ) : (
    <div className={`appearance-none block w-full ${editMode ? 'bg-white' : 'bg-gray-200'} text-gray-700 border rounded py-3 px-4 m-1 focus:outline-gray leading-tight`}>
      {value}
    </div>
  );
};

export default Dropdown;
