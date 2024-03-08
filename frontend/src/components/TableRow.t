import React, { useState } from 'react';
import { MobileTimePicker} from '@mui/x-date-pickers';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';

const TableRow = ({schedulingData, deleteRow}) => {
  const initialData = {
    program: 'Select',
    startTime: '00:00 AM',
    endTime: '00:00 AM',
    course: 'Select',
    instructor: 'Select',
    room: 'Select',
  };

  const [data, setData] = useState(initialData);
  const [editMode, setEditMode] = useState(false);

  const handleEdit = () => {
    setEditMode(!editMode);
  };

  const handleSave = () => {
    // console.log(data.startTime)
    setEditMode(false);
  };

  const handleChange = (value, field) => {
    setData({ ...data, [field]: value });
  };

  return (
    <div className="overflow-x-auto">
      <table className="min-w-full bg-white border border-gray-300">
        <tbody>
          <tr className="grid grid-cols-7">
            <td className="py-2 px-4 border-b">
            {editMode ? (
            <div className="relative">
              <select
                className={`appearance-none block w-full bg-white text-gray-700 border rounded py-3 px-4 m-1 focus:outline-gray leading-tight`}
                value={data.program}
                onChange={(e) => handleChange(e.target.value, 'program')}
              >
                {schedulingData.programs.map((program, index) => (
                  <option key={index} value={program}>
                    {program}
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
              {data.program}
            </div>
          )}

            </td>
            <td className="py-2 px-4 border-b">
              <LocalizationProvider dateAdapter={AdapterDayjs}>
                <MobileTimePicker
                  className={`appearance-none block w-full ${editMode ? 'bg-white' : 'bg-gray-200'} text-gray-700 border rounded py-3 px-4 m-1 focus:outline-gray leading-tight`}
                  value={data.startTime}
                  onChange={(newValue) => handleChange(newValue, 'startTime')}
                  disabled={!editMode}
                />   
              </LocalizationProvider>
            </td>
            <td className="py-2 px-4 border-b">
              <LocalizationProvider dateAdapter={AdapterDayjs}>
                <MobileTimePicker
                  className={`appearance-none block w-full ${editMode ? 'bg-white' : 'bg-gray-200'} text-gray-700 border rounded py-3 px-4 m-1 focus:outline-gray leading-tight`}
                  value={data.endTime}
                  onChange={(newValue) => handleChange(newValue, 'endTime')}
                  disabled={!editMode}
                />   
            </LocalizationProvider>
            </td>
            <td className="py-2 px-4 border-b">
              {editMode ? (
              <div className="relative">
                <select
                  className={`appearance-none block w-full bg-white text-gray-700 border rounded py-3 px-4 m-1 focus:outline-gray leading-tight`}
                  value={data.course}
                  onChange={(e) => handleChange(e.target.value, 'course')}
                >
                  {schedulingData.courses.map((course, index) => (
                    <option key={index} value={course}>
                      {course}
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
                {data.course}
              </div>
            )}
            </td>
            <td className="py-2 px-4 border-b">
              {editMode ? (
              <div className="relative">
                <select
                  className={`appearance-none block w-full bg-white text-gray-700 border rounded py-3 px-4 m-1 focus:outline-gray leading-tight`}
                  value={data.instructor}
                  onChange={(e) => handleChange(e.target.value, 'instructor')}
                >
                  {schedulingData.instructors.map((instructor, index) => (
                    <option key={index} value={instructor}>
                      {instructor}
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
                {data.instructor}
              </div>
            )}
            </td>
            <td className="py-2 px-4 border-b">
              {editMode ? (
              <div className="relative">
                <select
                  className={`appearance-none block w-full bg-white text-gray-700 border rounded py-3 px-4 m-1 focus:outline-gray leading-tight`}
                  value={data.room}
                  onChange={(e) => handleChange(e.target.value, 'room')}
                >
                  {schedulingData.rooms.map((room, index) => (
                    <option key={index} value={room}>
                      {room}
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
                {data.room}
              </div>
            )}
            </td>
            <td className="py-2 px-4 border-b grid grid-cols-2 gap-2">
              {editMode ? (
                <button 
                  onClick={handleSave}
                  className="text-green-500 hover:text-green-700">
                  Save
                </button>
              ) : (
                <button onClick={handleEdit} className="text-blue-500 hover:text-blue-700">
                  Edit
                </button>
              )}
              <button onClick={deleteRow} className="text-red-500 hover:text-red-700">
                Delete
                </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  );
};

export default TableRow;