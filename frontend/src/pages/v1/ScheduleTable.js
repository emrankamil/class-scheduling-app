import React, { useState } from 'react';
import Divider from '@mui/material/Divider';

import TableRow from '../../components/TableRow'

const ScheduleTable = () => {
  const [scheduleData, setScheduleData] = useState([
    { day: 'Monday', program: 'Program A', start_time: '9:00 AM', end_time: '11:00 AM', course: 'Math', instructor: 'John Doe', room: '101' },
    { day: 'Tuesday', program: 'Program B', start_time: '1:00 PM', end_time: '3:00 PM', course: 'Science', instructor: 'Jane Smith', room: '102' },
    { day: 'Wednesday', program: 'Program B', start_time: '1:00 PM', end_time: '3:00 PM', course: 'Science', instructor: 'Jane Smith', room: '102' },
    { day: 'Thursday', program: 'Program B', start_time: '1:00 PM', end_time: '3:00 PM', course: 'Science', instructor: 'Jane Smith', room: '102' },
    { day: 'Friday', program: 'Program B', start_time: '1:00 PM', end_time: '3:00 PM', course: 'Science', instructor: 'Jane Smith', room: '102' },
    
  ]);

  const schedulingData = {
    programs: ['Program A', 'Program B', 'Program C'],
    instructors: ['Instructor X', 'Instructor Y', 'Instructor Z'],
    courses: ['Course 101', 'Course 202', 'Course 303'],
    rooms: ['Room 1', 'Room 2', 'Room 3'],
    timeSlots: [
      '09:00 AM - 10:00 AM',
      '10:00 AM - 11:00 AM',
      '11:00 AM - 12:00 PM',
      '01:00 PM - 02:00 PM',
      '02:00 PM - 03:00 PM',
      '03:00 PM - 04:00 PM',
    ],
  };


  const [numRows, setNumRows] = useState({});

  const addRow = (day) => {
    setNumRows((prevNumRows) => ({ ...prevNumRows, [day]: (prevNumRows[day] || 0) + 1 }));
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

      {scheduleData.map((row, index) => (
        <React.Fragment key={index}>
          <div className="col-span-1 flex flex-col">
            <div>{row.day}</div>
            <button className="bg-gray-100 hover:bg-gray-200 py-1 px-1 rounded border-2"
             onClick={() => addRow(row.day)}>Add New Program</button>
          </div>
          <div className="col-span-7">
            <div className="w-full h-full bg-gray-200 flex flex-col">
              {[...Array(numRows[row.day] || 0)].map((_, rowIndex) => (
                <TableRow key={rowIndex} rowData={row} deleteRow={() => deleteRow(row.day)} schedulingData={schedulingData}/>
              ))}
            </div>
          </div>
        </React.Fragment>
      ))}
    </div>
  );
};

export default ScheduleTable;

