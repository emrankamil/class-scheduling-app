import React, { useState } from 'react';
// import Divider from '@mui/material/Divider';

import TableRow from '../../components/TableRow'

const DefaultRow = () => {
  return (
    <div className="overflow-x-auto">
      <table className="min-w-full bg-white border border-gray-300">
        <tbody>
          <tr className="grid grid-cols-7">
            <td className="py-2 px-4 border-b">
            <div className={`appearance-none block w-full text-gray-700 bg-gray-200 border rounded py-3 px-4 m-1 focus:outline-gray leading-tight`}>
              Lunch Break
            </div>

            </td>
            <td className="py-2 px-4 border-b">
              <div className={`appearance-none block w-full text-gray-700 bg-gray-200 border rounded py-3 px-4 m-1 focus:outline-gray leading-tight`}>
                12:00PM
              </div>
            </td>
            <td className="py-2 px-4 border-b">
              <div className={`appearance-none block w-full text-gray-700 bg-gray-200 border rounded py-3 px-4 m-1 focus:outline-gray leading-tight`}>
                2:00PM
              </div>
            </td>
            
          </tr>
        </tbody>
      </table>
    </div>
  )
}

const ScheduleTable = () => {
  const days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
  
  const schedulingData = {
    programs: ['Select','Lecture ', 'Break'],
    instructors: ['Select','Instructor X', 'Instructor Y', 'Instructor Z'],
    courses: ['Select','Course 101', 'Course 202', 'Course 303'],
    rooms: ['Select','Room 1', 'Room 2', 'Room 3'],
    timeSlots: [
      '09:00 AM - 10:00 AM',
      '10:00 AM - 11:00 AM',
      '11:00 AM - 12:00 PM',
      '01:00 PM - 02:00 PM',
      '02:00 PM - 03:00 PM',
      '03:00 PM - 04:00 PM',
    ],
  };

  const finalData = [
    {Monday: {
      1: {program:'Lecture', instructor: 'Abebe', course:'Fundamental', room:'210', startTime:'17:00', endTime:'19:00'},
      2: {program:'Break', instructor: 'Abebech', course:'Fundamentals', room:'201', startTime:'19:00', endTime:'20:00'},
      3: {program:'Lecture', instructor: 'Abebk', course:'Fundamental', room:'210', startTime:'01:00', endTime:'02:00'},
    }},
    {Monday: {
      1: {program:'Lecture', instructor: 'Alemseged', course:'Fundamental', room:'210', startTime:'17:00', endTime:'19:00'},
      2: {program:'Break', instructor: 'Abebech', course:'Fundamentals', room:'201', startTime:'19:00', endTime:'20:00'},
      3: {program:'Lecture', instructor: 'Abebk', course:'Fundamental', room:'210', startTime:'01:00', endTime:'02:00'},
    }},
    {Monday: {
      1: {program:'Lecture', instructor: 'Alemseged', course:'Fundamental', room:'210', startTime:'17:00', endTime:'19:00'},
      2: {program:'Break', instructor: 'Abebech', course:'Fundamentals', room:'201', startTime:'19:00', endTime:'20:00'},
      3: {program:'Lecture', instructor: 'Abebk', course:'Fundamental', room:'210', startTime:'01:00', endTime:'02:00'},
    }},
    {Monday: {
      1: {program:'Lecture', instructor: 'Abebe', course:'Fundamental', room:'210', startTime:'17:00', endTime:'19:00'},
      2: {program:'Break', instructor: 'Abebech', course:'Fundamentals', room:'201', startTime:'19:00', endTime:'20:00'},
      3: {program:'Lecture', instructor: 'Abebk', course:'Fundamental', room:'210', startTime:'01:00', endTime:'02:00'},
    }},
    {Monday: {
      1: {program:'Lecture', instructor: 'Abebe', course:'Fundamental', room:'210', startTime:'17:00', endTime:'19:00'},
      2: {program:'Break', instructor: 'Abebech', course:'Fundamentals', room:'201', startTime:'19:00', endTime:'20:00'},
      3: {program:'Lecture', instructor: 'Abebk', course:'Fundamental', room:'210', startTime:'01:00', endTime:'02:00'},
    }}
  ]

  const [numRows, setNumRows] = useState({});

  const addRow = (day) => {
    setNumRows((prevNumRows) => ({ ...prevNumRows, [day]: (prevNumRows[day] || 0) + 1 }));
    console.log(numRows)
  };

  const saveRow = (day, index, newData) => {
    finalData[day][index] = newData;
  };

  const deleteRow = (day) => {
    if (numRows[day] > 0) {
      setNumRows((prevNumRows) => ({ ...prevNumRows, [day]: prevNumRows[day] - 1 }));
    }
  };

  return (
    <div className="grid grid-cols-8 gap-4 m-4">
      <div className="col-span-1">Day</div>
      <div className="col-span-1">Program</div>
      <div className="col-span-1">Start Time</div>
      <div className="col-span-1">End Time</div>
      <div className="col-span-1">Course</div>
      <div className="col-span-1">Instructor</div>
      <div className="col-span-1">Room</div>
      <div className="col-span-1">Actions</div>

      {days.map((day, index) => [
        <div key={index} className="col-span-1 flex flex-col my-2 border-2">
          <div>{day}</div>
          <button className="bg-gray-100 hover:bg-gray-200 py-1 px-1 rounded border-2" onClick={() => addRow(day)}>
            Add New Program
          </button>
        </div>,
        <div key={`content-${index}`} className="col-span-7 my-2 border-2">
          <div className="w-full h-full bg-gray-200 flex flex-col">
              <DefaultRow />
            {[...Array(numRows[day] || 0)].map((_, rowIndex) => (
              <TableRow key={rowIndex} deleteRow={() => deleteRow(day)} schedulingData={schedulingData} />
            ))}
          </div>
        </div>,
      ])}
    </div>
  );
};

export default ScheduleTable;

