import React, { useState } from 'react';

const TableRow = ({schedulingData, rowData, deleteRow}) => {
  const initialData = {
    program: 'Program',
    startTime: '00:00 AM',
    endTime: '00:00 AM',
    course: 'Course',
    instructor: 'Instructor',
    room: 'Room',
  };

  const [data, setData] = useState(initialData);
  const [editMode, setEditMode] = useState(false);

  const handleEdit = () => {
    setEditMode(!editMode);
  };

  const handleSave = () => {
    // Save logic goes here, you can update your backend or local state
    setEditMode(false);
  };

  const handleChange = (e, field) => {
    setData({ ...data, [field]: e.target.value });
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
                onChange={(e) => handleChange(e, 'program')}
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
              <input
                className={`appearance-none block w-full ${editMode ? 'bg-white' : 'bg-gray-200'} text-gray-700 border rounded py-3 px-4 m-1 focus:outline-gray leading-tight`}
                type="text"
                value={data.startTime}
                onChange={(e) => handleChange(e, 'startTime')}
                disabled={!editMode}
              />
            </td>
            <td className="py-2 px-4 border-b">
              <input
                className={`appearance-none block w-full ${editMode ? 'bg-white' : 'bg-gray-200'} text-gray-700 border rounded py-3 px-4 m-1 focus:outline-gray leading-tight`}
                type="text"
                value={data.endTime}
                onChange={(e) => handleChange(e, 'endTime')}
                disabled={!editMode}
              />
            </td>
            <td className="py-2 px-4 border-b">
              <input
                className={`appearance-none block w-full ${editMode ? 'bg-white' : 'bg-gray-200'} text-gray-700 border rounded py-3 px-4 m-1 focus:outline-gray leading-tight`}
                type="text"
                value={data.course}
                onChange={(e) => handleChange(e, 'course')}
                disabled={!editMode}
              />
            </td>
            <td className="py-2 px-4 border-b">
              <input
                className={`appearance-none block w-full ${editMode ? 'bg-white' : 'bg-gray-200'} text-gray-700 border rounded py-3 px-4 m-1 focus:outline-gray leading-tight`}
                type="text"
                value={data.instructor}
                onChange={(e) => handleChange(e, 'instructor')}
                disabled={!editMode}
              />
            </td>
            <td className="py-2 px-4 border-b">
              <input
                className={`appearance-none block w-full ${editMode ? 'bg-white' : 'bg-gray-200'} text-gray-700 border rounded py-3 px-4 m-1 focus:outline-gray leading-tight`}
                type="text"
                value={data.room}
                onChange={(e) => handleChange(e, 'room')}
                disabled={!editMode}
              />
            </td>
            <td className="py-2 px-4 border-b grid grid-cols-2 gap-2">
              {editMode ? (
                <button onClick={handleSave} className="text-green-500 hover:text-green-700">
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