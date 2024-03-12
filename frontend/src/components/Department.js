import {useEffect, useState} from 'react';
import Accordion from '@mui/material/Accordion';
import AccordionActions from '@mui/material/AccordionActions';
import AccordionSummary from '@mui/material/AccordionSummary';
import AccordionDetails from '@mui/material/AccordionDetails';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import Button from '@mui/material/Button';
import {FormLabel,FormControlLabel, FormControl,
     FormGroup, Grid, Checkbox, InputAdornment,
    TextField,} from '@mui/material';

export default function Department({department, courses, instructors, onChange}) {

    const [isEditMode, setIsEditMode] = useState(false);
    const [disableInput, setDisableInput] = useState(false);

    const [state, setState] = useState({
        monday: true,
        tuesday: false,
        wednesday: false,
        thrusday: false,
        friday: false,
        saturday: false,
    });
    const { monday, tuesday, wednesday, thrusday, friday, saturday} = state;

    const { name, assigned_days, morning_start_time, morning_end_time, afternoon_start_time, afternoon_end_time } = department;
    
    const handleEditClick = () => {
        setIsEditMode(!isEditMode);
    };

    return (
        <Accordion>
        <AccordionSummary
        expandIcon={<ExpandMoreIcon />}
        aria-controls="panel3-content"
        id="panel3-header"
        >
        {name}
        </AccordionSummary>
        <AccordionDetails>
        <form className="w-full">
            <div className="flex flex-wrap -mx-3 mb-6">
                <div className="w-full px-3">
                <label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2">
                    Department
                </label>
                <input className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" id="department-name" placeholder={name} disabled={disableInput}></input>
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
            <CourseDropdown/>
            <div className="flex flex-wrap -mx-3 m-4">
                <div className="w-full md:w-1/2 px-3 mb-6 md:mb-0">
                <Grid item xs={6}>
                    <FormControl component="fieldset">
                        <FormLabel component="legend">Assigned Days</FormLabel>
                        <FormGroup className='flex flex-wrap'>
                            <FormControlLabel
                                control={<Checkbox checked={monday} onChange={()=>onChange()} name="monday" />}
                                label="Monday"
                            />
                            <FormControlLabel
                                control={<Checkbox checked={tuesday} onChange={()=>onChange()} name="tuesday" />}
                                label="Tuesday"
                            />
                            <FormControlLabel
                                control={<Checkbox checked={wednesday} onChange={()=>onChange()} name="wednesday" />}
                                label="Wednesday"
                            />
                            <FormControlLabel
                                control={<Checkbox checked={thrusday} onChange={()=>onChange()} name="thrusday" />}
                                label="Thrusday"
                            />
                            <FormControlLabel
                                control={<Checkbox checked={friday} onChange={()=>onChange()} name="friday" />}
                                label="Friday"
                            />
                            <FormControlLabel
                                control={<Checkbox checked={saturday} onChange={()=>onChange()} name="saturday" />}
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
                    <CourseDropdown/>
                </div>
            </form>
        </AccordionDetails>
        <AccordionActions>
        <Button>Save</Button>
        <Button onClick={handleEditClick}>Edit</Button>
        <Button>Continue</Button>
        </AccordionActions>
        </Accordion>
    )

}


const DisplayContent = ({ value }) => (
    <div className="appearance-none block w-full bg-gray-200 text-gray-700 border rounded py-3 px-4 m-1 leading-tight focus:outline-none focus:bg-white">
        {value}
    </div>
);

const InputField = ({ placeholder, disabled }) => (
    <input
        type="text"
        placeholder={placeholder}
        disabled={disabled}
        className="w-full appearance-none block bg-gray-200 text-gray-700 border rounded py-3 px-4 m-1 leading-tight focus:outline-none focus:bg-white"
    />
);

const CourseDropdown = () => {
    const [isEditMode, setIsEditMode] = useState(false);
    const [courses, setCourses] = useState([
      { name: 'Course 1', creditHours: 3 },
      { name: 'Course 2', creditHours: 4 },
      // Add more initial courses as needed
    ]);
  
    const handleAddCourse = () => {
      // Add your logic to handle adding a new course
      const newCourse = { name: 'New Course', creditHours: 0 };
      setCourses([...courses, newCourse]);
      setIsEditMode(true); // Automatically switch to edit mode for the newly added course
    };
  
    const handleDeleteCourse = (index) => {
      // Add your logic to handle deleting a course
      const updatedCourses = [...courses];
      updatedCourses.splice(index, 1);
      setCourses(updatedCourses);
    };
  
    const handleEditCourse = (index, newName, newCreditHours) => {
      // Add your logic to handle editing a course name and credit hours
      const updatedCourses = [...courses];
      updatedCourses[index].name = newName;
      updatedCourses[index].creditHours = newCreditHours;
      setCourses(updatedCourses);
    };
  
    return (
      <Accordion className="my-3">
        <AccordionSummary
          expandIcon={<ExpandMoreIcon />}
          aria-controls="panel1-content"
          id="panel1-header"
        >
          Courses
        </AccordionSummary>
        <AccordionDetails>
          <div className="w-full">
            {courses.map((course, index) => (
              <div key={index} className="flex items-center my-2">
                <TextField
                  type="text"
                  label="Course Name"
                  value={course.name}
                  onChange={(e) => handleEditCourse(index, e.target.value, course.creditHours)}
                  className="w-3/4"
                />
                <TextField
                  type="number"
                  label="Credit Hours"
                  value={course.credit_hour}
                  onChange={(e) => handleEditCourse(index, course.name, e.target.value)}
                  InputProps={{ startAdornment: <InputAdornment position="start">hrs</InputAdornment> }}
                  className="ml-2"
                />
                <Button
                  onClick={() => handleDeleteCourse(index)}
                  // color="secondary"
                  // variant="contained"
                  className="ml-2"
                >
                  Delete
                </Button>
              </div>
            ))}
          </div>
        </AccordionDetails>
        <AccordionActions>
          <Button onClick={handleAddCourse}>
            Add
          </Button>
          <Button onClick={() => setIsEditMode(!isEditMode)}>
            {isEditMode ? 'Save' : 'Edit'}
          </Button>
        </AccordionActions>
      </Accordion>
    );
  };
