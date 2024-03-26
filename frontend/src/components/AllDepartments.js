import {useEffect, useState} from 'react';
import Department from './Department';

export default function AllDepartments() {

    const departmentsData_url = "http://localhost:8000/api/departments_config/departments_data/"

    const [disableInput, setDisableInput] = useState(true)
    const [departmentData, setDepartmentData] = useState(null)
    const [instructorData, setInstructorData] = useState(null)
    const [courseData, setCourseData] = useState(null)

    const [state, setState] = useState({
        monday: true,
        tuesday: false,
        wednesday: false,
        thrusday: false,
        friday: false,
        saturday: false,
    });
    const { monday, tuesday, wednesday, thrusday, friday, saturday} = state;

    const handleChange = (event) => {
        setState({ ...state, [event.target.name]: event.target.checked });
    };

    // const handleEdit = () => {
    //     setDisableInput(!editMode);
    //   };

    useEffect(() => {
        const fetchData = async () => {
          try {
            const response = await fetch(departmentsData_url);
      
            if (!response.ok) {
              throw new Error(`HTTP error! Status: ${response.status}`);
            }

            const data = await response.json();
            // console.log(response.json())
      
            setDepartmentData(data.departments);
            setInstructorData(data.instructors);
            setCourseData(data.courses);
            console.log(departmentData)

          } catch (error) {
            console.error('Error fetching data:', error);
          }
        };
      
        fetchData();
      }, []);
      
    

    if(!departmentData){
        return(
          <div>
            <p>No History </p>
          </div>
        )
    }

  return (
    <div className='flex flex-col gap-4 w-5/6 mx-auto '>
        {departmentData.map((department, index)=>{ 
            const filteredCourses = courseData.filter(item => department.courses.includes(item['id']));
            const filteredInstructors = instructorData.filter(item => department.instructors.includes(item['id']));         
            return <Department key={index} department={department} courses={filteredCourses} instructors={filteredInstructors} onChange={handleChange}/>        
        } )}
    </div>
  );
}
