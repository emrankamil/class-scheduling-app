import React, { useState } from 'react';

const RecursiveBox = ({ remainingHeight, onBoxClick, label, isDisabled}) => {
  const [divided, setDivided] = useState(false);
  const [showPopup, setShowPopup] = useState(false);
  const [startInput, setStartInput] = useState('');
  const [endInput, setEndInput] = useState('');

  const handleBoxClick = () => {
    if (!divided) {
      setShowPopup(true);
    }
  };

  const handleConfirmClick = () => {
    setDivided(true);
    onBoxClick(`${startInput}-${endInput}`); /* will call the handleboxClick */
    setShowPopup(false);
  };

  return (
    <div
      style={{ height: `${remainingHeight}px`, border: '0.5px solid gray', cursor: 'pointer' }}
      onClick={handleBoxClick}
      disabled={isDisabled}
    >
      {!divided && <div>{label}</div>}
      {showPopup && (
        <div style={{ position: 'absolute', top: '50%', left: '50%', transform: 'translate(-50%, -50%)', padding: '10px', background: 'white', zIndex: '100' }}>
          <label htmlFor="startInput">Start:</label>
          <input
            type="text"
            id="startInput"
            value={startInput}
            onChange={(e) => setStartInput(e.target.value)}
          />
          <br />
          <label htmlFor="endInput">End:</label>
          <input
            type="text"
            id="endInput"
            value={endInput}
            onChange={(e) => setEndInput(e.target.value)}
          />
          <br />
          <button onClick={handleConfirmClick}>Confirm</button>
        </div>
      )}

      {divided && (
        <>
          <RecursiveBox remainingHeight={remainingHeight / 2} onBoxClick={onBoxClick} label={`${label.split('-')[0]}-${startInput}`} isDisabled={false}/>
          <RecursiveBox remainingHeight={remainingHeight / 2} onBoxClick={onBoxClick} label={`${endInput}-${label.split('-')[1]}`} isDisabled={false}/>
        </>
      )}
    </div>
  );
};

const Box = () => {
  const overallHeight = 200;

  const handleBoxClick = (label) => {
    console.log(`Box clicked with label: ${label}`);
  };

  return (
    <div>
      <RecursiveBox remainingHeight={overallHeight} onBoxClick={handleBoxClick} label="1-10" isDisabled={true}/>
    </div>
  );
};

export default Box;


