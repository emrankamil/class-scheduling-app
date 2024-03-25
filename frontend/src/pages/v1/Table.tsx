import React from 'react';
import Box from '../../components/Box'
import { useParams } from 'react-router-dom';

const Timetable = () => {

  const {id} = useParams()
  
  return (
    <div className="grid grid-cols-6 gap-2 px-4 my-4">
      <div className="col-span-1 h-16 border-2 flex items-center justify-center">Time</div>
      <div className="col-span-1 h-16 border-2 flex items-center justify-center">Monday</div>
      <div className="col-span-1 h-16 border-2 flex items-center justify-center">Tuesday</div>
      <div className="col-span-1 h-16 border-2 flex items-center justify-center">Wednesday</div>
      <div className="col-span-1 h-16 border-2 flex items-center justify-center">Thursday</div>
      <div className="col-span-1 h-16 border-2 flex items-center justify-center">Friday</div>

      <div className="col-span-1 border-2 flex items-center justify-center">2:00-6:00</div>
      <div className="col-span-1 border-2">A</div>
      <div className="col-span-1 border-2">A</div>
      <div className="col-span-1 border-2">A</div>
      <div className="col-span-1 border-2">A</div>
      <div className="col-span-1 border-2">A</div>

      <div className="col-span-1 border-2 flex items-center justify-center">6:00-8:00</div>
      <div className="col-span-1 border-2">A</div>
      <div className="col-span-1 border-2">A</div>
      <div className="col-span-1 border-2">A</div>
      <div className="col-span-1 border-2">A</div>
      <div className="col-span-1 border-2">A</div>

      <div className="col-span-1 border-2 flex items-center justify-center">8:00-11:00</div>
      <div className="col-span-1 border-2">A</div>
      <div className="col-span-1 border-2">A</div>
      <div className="col-span-1 border-2">A</div>
      <div className="col-span-1 border-2">A</div>
      <div className="col-span-1 border-2">A</div>
    </div>
  );
};

export default Timetable;
