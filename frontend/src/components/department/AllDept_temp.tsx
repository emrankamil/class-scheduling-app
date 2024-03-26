import React, { useState } from 'react';
import api from '../../api/posts'
import { Link } from 'react-router-dom';

// interface DepartmentFormProps {
//   onSubmit: (formData: DepartmentFormData) => void;
// }

interface DepartmentFormData {
  name: string;
  courses: {
    name: string;
    credit_hour: number;
  }[];

  instructors: {name:string}[];
  assignedDays: string[];
  rooms: string[];
  morningStartTime: string;
  morningEndTime: string;
  afternoonStartTime: string;
  afternoonEndTime: string;
}

interface Course {
  name: string;
  credit_hour: number;
}

interface InputEvent extends React.ChangeEvent<HTMLInputElement> {
  target: HTMLInputElement & {
    name: keyof Course;
    value: string;
  };
}

const DepartmentForm = () => {
  const [formData, setFormData] = useState<DepartmentFormData>({
    name: '',
    courses: [],
    instructors: [],
    assignedDays: [],
    rooms: [],
    morningStartTime: '00:00:00',
    morningEndTime: '00:00:00',
    afternoonStartTime: '00:00:00',
    afternoonEndTime: '00:00:00',
  });

  const [departmentId, setDepartmetid] = useState(0)

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  // const handleArrayChange = (e: React.ChangeEvent<HTMLInputElement>, fieldName: string) => {
  //   const { value } = e.target;
  //   setFormData({ ...formData, [fieldName]: value.split(',') });
    
  // };

  const handleArrayChange = (e: React.ChangeEvent<HTMLInputElement>, fieldName: string) => {
    const { value, name } = e.target;
    if (name == 'instructors'){
      const parsedInstructors = value.split(',').map((name, index) => ({name }));
      setFormData({ ...formData, [fieldName]: parsedInstructors });
    }else{
      setFormData({ ...formData, [fieldName]: value.split(',') });
    }
  };

  
  const handleCourseInputChange = (e: InputEvent, index: number) => {
    const { name, value } = e.target;
    setFormData(prevFormData => {
      const newCourses = [...prevFormData.courses];
      newCourses[index] = { ...newCourses[index], [name]: value };
      return { ...prevFormData, courses: newCourses };
    });
  };

  const handleAddCourse = () => {
    setFormData(prevFormData => ({
      ...prevFormData,
      courses: [...prevFormData.courses, { name: '', credit_hour: 0 }]
    }));
  };
  
  
  const handleSubmit =async (e: React.FormEvent) => {
    e.preventDefault();

    const transformedData = {
      departments: formData,
      courses: formData.courses,
      instructors: formData.instructors
    };

    try{
      const response = await api.post('departments_config/departments_data/', transformedData)
      setDepartmetid(response.data.department_id)
      console.log('Form Submitted Succesfully')
    }catch{
      console.log(`error`)
    }
  };
  

  return (
    <form onSubmit={handleSubmit} className="max-w-md mx-auto mt-8">
      <div className="mb-4">
        <label htmlFor="name" className="block text-sm font-medium text-gray-700">Department Name</label>
        <input type="text" id="name" name="name" value={formData.name} onChange={handleChange} className="mt-1 p-2 border border-gray-300 rounded-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm" />
      </div>

      {/* courses section */}
      <div className="w-full max-w-md mx-auto">
        {formData.courses.map((course, index) => (
          <div key={index} className="mb-4">
            <input
              type="text"
              name="name"
              placeholder="Course Name"
              value={course.name}
              onChange={(e) => handleCourseInputChange(e as InputEvent, index)}
              className="w-1/2 px-3 py-2 border rounded-md focus:outline-none focus:ring focus:border-blue-300"
            />
            <input
              type="number"
              name="credit_hour"
              placeholder="Credit Hour"
              value={course.credit_hour}
              onChange={(e) => handleCourseInputChange(e as InputEvent, index)}
              className="w-1/4 ml-2 px-3 py-2 border rounded-md focus:outline-none focus:ring focus:border-blue-300"
            />
          </div>
        ))}
        <button
          onClick={handleAddCourse}
          className="bg-blue-500 text-white px-4 py-2 rounded-md hover:bg-blue-600 focus:outline-none focus:ring focus:border-blue-300"
        >
          Add Course
        </button>
      </div>

      {/* Instructors Section */}
      <div className="mb-4">
        <label htmlFor="instructors" className="block text-sm font-medium text-gray-700">Instructors (comma-separated)</label>
        <input 
          type="text" 
          id="instructors" 
          name="instructors" 
          value={formData.instructors.map(instructor => instructor.name).join(',')} 
          onChange={(e) => handleArrayChange(e, 'instructors')} 
          className="mt-1 p-2 border border-gray-300 rounded-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm" 
        />
      </div>


      <div className="mb-4">
        <label htmlFor="assignedDays" className="block text-sm font-medium text-gray-700">Assigned Days (comma-separated)</label>
        <input type="text" id="assignedDays" name="assignedDays" value={formData.assignedDays.join(',')} onChange={(e) => handleArrayChange(e, 'assignedDays')} className="mt-1 p-2 border border-gray-300 rounded-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm" />
      </div>

      <div className="mb-4">
        <label htmlFor="rooms" className="block text-sm font-medium text-gray-700">Rooms (comma-separated)</label>
        <input type="text" id="rooms" name="rooms" value={formData.rooms.join(',')} onChange={(e) => handleArrayChange(e, 'rooms')} className="mt-1 p-2 border border-gray-300 rounded-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm" />
      </div>
      
      <div className="mb-4">
        <label htmlFor="morningStartTime" className="block text-sm font-medium text-gray-700">Morning Start Time</label>
        <input type="time" id="morningStartTime" name="morningStartTime" value={formData.morningStartTime} onChange={handleChange} className="mt-1 p-2 border border-gray-300 rounded-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm" />
      </div>
      <div className="mb-4">
        <label htmlFor="morningEndTime" className="block text-sm font-medium text-gray-700">Morning End Time</label>
        <input type="time" id="morningEndTime" name="morningEndTime" value={formData.morningEndTime} onChange={handleChange} className="mt-1 p-2 border border-gray-300 rounded-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm" />
      </div>
      <div className="mb-4">
        <label htmlFor="afternoonStartTime" className="block text-sm font-medium text-gray-700">Afternoon Start Time</label>
        <input type="time" id="afternoonStartTime" name="afternoonStartTime" value={formData.afternoonStartTime} onChange={handleChange} className="mt-1 p-2 border border-gray-300 rounded-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm" />
      </div>
      <div className="mb-4">
        <label htmlFor="afternoonEndTime" className="block text-sm font-medium text-gray-700">Afternoon End Time</label>
        <input type="time" id="afternoonEndTime" name="afternoonEndTime" value={formData.afternoonEndTime} onChange={handleChange} className="mt-1 p-2 border border-gray-300 rounded-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm" />
      </div>

      <div className="mt-4">
        <button type="submit" className="inline-flex justify-center py-2 px-4 border border-transparent shadow-sm text-sm font-medium rounded-md text-black bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
          Save
        </button>
      </div>

        {/* <Link
              to={`/v1/class/schedule/${departmentId}`}
              className="inline-flex justify-center py-2 px-4 border border-transparent shadow-sm text-sm font-medium rounded-md text-black bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
            >
              Continue
          </Link> */}
      <div className="mt-4">
        {departmentId !== 0 ? (
          <Link
            to={`/v1/class/schedule/${departmentId}`}
            className="inline-flex justify-center py-2 px-4 border border-transparent shadow-sm text-sm font-medium rounded-md text-black bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
          >
            Continue
          </Link>
        ) : (
          <button
            className="inline-flex justify-center py-2 px-4 border border-transparent shadow-sm text-sm font-medium rounded-md text-black bg-gray-300 cursor-not-allowed"
            disabled
          >
            Continue
          </button>
        )}
      </div>

    </form>
  );
};

export default DepartmentForm;
