import {useEffect, useState} from 'react';
import Accordion from '@mui/material/Accordion';
import AccordionActions from '@mui/material/AccordionActions';
import AccordionSummary from '@mui/material/AccordionSummary';
import AccordionDetails from '@mui/material/AccordionDetails';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import Button from '@mui/material/Button';
import {FormLabel,FormControlLabel, FormControl, FormGroup, Grid, Checkbox} from '@mui/material';

export default function Department() {

    const departmentsData_url = 'http://localhost:8000/api/departments_data/'

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

    useEffect(() => {
        const fetchData = async () => {
          try {
            const response = await fetch(departmentsData_url);
      
            if (!response.ok) {
              throw new Error(`HTTP error! Status: ${response.status}`);
            }

            // console.log(response.json())
            const data = await response.json();
      
            setDepartmentData(data.departments);
            setInstructorData(data.instructors);
            setCourseData(data.courses);

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

    const handleChange = (event) => {
        setState({ ...state, [event.target.name]: event.target.checked });
    };

  return (
    <div className='flex flex-col gap-4 w-5/6 mx-auto '>
        <div>Hello</div>
        {departmentData.map((department, index)=>{

            const { name, courses, instructors, assigned_days, morning_start_time, morning_end_time, afternoon_start_time, afternoon_end_time } = department;
            
            const filteredCourses = courseData.filter(item => courses.includes(item['id']));
            const filteredInstructors = instructorData.filter(item => instructors.includes(item['id']));
            
            return (
                <Accordion key={index}>
                <AccordionSummary
                expandIcon={<ExpandMoreIcon />}
                aria-controls="panel3-content"
                id="panel3-header"
                >
                Accordion Actions
                </AccordionSummary>
                <AccordionDetails>
                <form className="w-full">
                    <div className="flex flex-wrap -mx-3 mb-6">
                        <div className="w-full px-3">
                        <label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor="grid-password">
                            Department
                        </label>
                        <input className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" id="department-name" type="password" placeholder={name} disabled={disableInput}></input>
                        </div>
                    </div>
                    <div className="flex -mx-3 mb-2">
                        <div className="w-full md:w-1/2 px-3 md:mb-0">
                        <label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor="courses">
                            Courses
                        </label>
                        </div>
                        <div className="w-full md:w-1/2 px-3">
                        <label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor="credit-hour">
                            Credit Hour

                        </label>
                        </div>
                    </div>
                    {filteredCourses.map((course, index)=>{
                        return(
                        <div className="flex -mx-3" key={index}>
                            <input className="appearance-none block w-full bg-gray-200 text-gray-700 border rounded py-3 px-4 m-1 leading-tight focus:outline-none focus:bg-white" type="text" placeholder={course.name} disabled={disableInput}></input>
                            <input className="appearance-none block w-full bg-gray-200 text-gray-700 border rounded py-3 px-4 m-1 leading-tight focus:outline-none focus:bg-white" type="text" placeholder={course.credit_hour} disabled={disableInput}></input>      
                        </div>)
                    })
                    }
                    <div className="flex flex-wrap -mx-3 m-4">
                        <div className="w-full md:w-1/2 px-3 mb-6 md:mb-0">
                        <Grid item xs={6}>
                            <FormControl component="fieldset">
                                <FormLabel component="legend">Assigned Days</FormLabel>
                                <FormGroup className='flex flex-wrap'>
                                    <FormControlLabel
                                        control={<Checkbox checked={monday} onChange={handleChange} name="monday" />}
                                        label="Monday"
                                    />
                                    <FormControlLabel
                                        control={<Checkbox checked={tuesday} onChange={handleChange} name="tuesday" />}
                                        label="Tuesday"
                                    />
                                    <FormControlLabel
                                        control={<Checkbox checked={wednesday} onChange={handleChange} name="wednesday" />}
                                        label="Wednesday"
                                    />
                                    <FormControlLabel
                                        control={<Checkbox checked={thrusday} onChange={handleChange} name="thrusday" />}
                                        label="Thrusday"
                                    />
                                    <FormControlLabel
                                        control={<Checkbox checked={friday} onChange={handleChange} name="friday" />}
                                        label="Friday"
                                    />
                                    <FormControlLabel
                                        control={<Checkbox checked={saturday} onChange={handleChange} name="saturday" />}
                                        label="Saturday"
                                    />
                                </FormGroup>
                            </FormControl>
                        </Grid>
                        </div>
                        <div className="w-full md:w-1/2 px-3 mb-6 md:mb-0">
                            <div className='flex'>
                                <div className='bg-gray-200 text-gray-700 border rounded py-3 px-4 m-1'>Morning Session Starts At</div>
                                <div className='bg-gray-200 text-gray-700 border rounded py-3 px-4 m-1'>{morning_start_time}</div>
                            </div>
                            <div className='flex'>
                                <div className='bg-gray-200 text-gray-700 border rounded py-3 px-4 m-1'>Morning Session Ends At</div>
                                <div className='bg-gray-200 text-gray-700 border rounded py-3 px-4 m-1'>{morning_end_time}</div>
                            </div>
                            <div className='flex'>
                                <div className='bg-gray-200 text-gray-700 border rounded py-3 px-4 m-1'>Afternoon Session Starts At</div>
                                <div className='bg-gray-200 text-gray-700 border rounded py-3 px-4 m-1'>{afternoon_start_time}</div>
                            </div>
                            <div className='flex'>
                                <div className='bg-gray-200 text-gray-700 border rounded py-3 px-4 m-1'>Afternoon Session Ends At</div>
                                <div className='bg-gray-200 text-gray-700 border rounded py-3 px-4 m-1'>{afternoon_end_time}</div>
                            </div>
                        </div>
                        
                        </div>
                        <div className="w-full md:w-1/3 px-3 mb-6 md:mb-0">
                            <Accordion key={index} className="my-3">
                                <AccordionSummary
                                expandIcon={<ExpandMoreIcon />}
                                aria-controls="panel3-content"
                                id="panel3-header"
                                >
                                Instructors
                                </AccordionSummary>
                                <AccordionDetails>
                                {disableInput ? (
                                    filteredInstructors.map((instructor, index) => (
                                        <div key={index} className="appearance-none block w-full bg-gray-200 text-gray-700 border rounded py-3 px-4 m-1 leading-tight focus:outline-none focus:bg-white" type="text" disabled={disableInput}>{instructor.name}</div>
                                    ))
                                    ) : (
                                    instructorData.map((instructor, index) => (
                                        <div key={index} className="appearance-none block w-full bg-gray-200 text-gray-700 border rounded py-3 px-4 m-1 leading-tight focus:outline-none focus:bg-white" type="text">{instructor.name}</div>
                                    ))
                                    )}
                                </AccordionDetails>
                                <AccordionActions>
                                    <Button>Add</Button>
                                </AccordionActions>
                            </Accordion>
                        </div>
                    </form>
                </AccordionDetails>
                <AccordionActions>
                <Button>Save</Button>
                <Button>Edit</Button>
                <Button>Continue</Button>
                </AccordionActions>
                </Accordion>
            )
        } )}
    </div>
  );
}
