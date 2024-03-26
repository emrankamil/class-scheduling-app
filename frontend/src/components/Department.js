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

export default function Department({department, courses, instructors, handleChange}) {

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


    // const handleChange = (e) => {
    //   const { name, value } = e.target;
    //   setFormData({ ...deaprtment, [name]: value });
    // };

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
                <input 
                  className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                   id="department-name" 
                   placeholder={name} 
                   disabled={disableInput}
                   onChange={handleChange}>

                </input>
                </div>
            </div>
            <div className="flex flex-wrap -mx-3 m-4">
                <div className="w-full md:w-1/2 px-3 mb-6 md:mb-0">
                <Grid item xs={6}>
                    <FormControl component="fieldset">
                        <FormLabel component="legend">Assigned Days</FormLabel>
                        <FormGroup className='flex flex-wrap'>
                            <FormControlLabel
                                control={<Checkbox checked={monday} onChange={()=>handleChange()} name="monday" />}
                                label="Monday"
                            />
                            <FormControlLabel
                                control={<Checkbox checked={tuesday} onChange={()=>handleChange()} name="tuesday" />}
                                label="Tuesday"
                            />
                            <FormControlLabel
                                control={<Checkbox checked={wednesday} onChange={()=>handleChange()} name="wednesday" />}
                                label="Wednesday"
                            />
                            <FormControlLabel
                                control={<Checkbox checked={thrusday} onChange={()=>handleChange()} name="thrusday" />}
                                label="Thrusday"
                            />
                            <FormControlLabel
                                control={<Checkbox checked={friday} onChange={()=>handleChange()} name="friday" />}
                                label="Friday"
                            />
                            <FormControlLabel
                                control={<Checkbox checked={saturday} onChange={()=>handleChange()} name="saturday" />}
                                label="Saturday"
                            />
                        </FormGroup>
                    </FormControl>
                </Grid>
                </div>
                <div className="w-full md:w-1/2 px-3 mb-6 md:mb-0">
                  <div className="mb-4">
                    <label htmlFor="morningStartTime" className="block text-sm font-medium text-gray-700">Morning Start Time</label>
                    <input 
                      type="time"
                      id="morningStartTime" 
                      name="morningStartTime" 
                      value={department.morning_start_time} 
                      className="mt-1 p-2 border border-gray-300 rounded-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm"
                      onChange={()=>handleChange()} />
                  </div>
                  <div className="mb-4">
                    <label htmlFor="morningEndTime" className="block text-sm font-medium text-gray-700">Morning End Time</label>
                    <input type="time" id="morningEndTime" name="morningEndTime" value={department.morning_end_time} className="mt-1 p-2 border border-gray-300 rounded-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm" onChange={()=>handleChange()}/>
                  </div>
                  <div className="mb-4">
                    <label htmlFor="afternoonStartTime" className="block text-sm font-medium text-gray-700">Afternoon Start Time</label>
                    <input type="time" id="afternoonStartTime" name="afternoonStartTime" value={department.afternoon_start_time} className="mt-1 p-2 border border-gray-300 rounded-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm" onChange={()=>handleChange()}/>
                  </div>
                  <div className="mb-4">
                    <label htmlFor="afternoonEndTime" className="block text-sm font-medium text-gray-700">Afternoon End Time</label>
                    <input type="time" id="afternoonEndTime" name="afternoonEndTime" value={department.afternoon_end_time} className="mt-1 p-2 border border-gray-300 rounded-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm" onChange={()=>handleChange()}/>
                  </div>
                </div>
                
                </div>
                <div className="w-full md:w-1/3 px-3 mb-6 md:mb-0">
                    <CourseDropdown/>
                </div>

                <div className="w-full md:w-1/3 px-3 mb-6 md:mb-0">
                    <InstructorDropdown/>
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


  
const InstructorDropdown = () => {
  const [isEditMode, setIsEditMode] = useState(false);
  const [instructors, setInstructors] = useState([
    { name: 'Instructor 1', creditHours: 3 },
    { name: 'Instructor 2', creditHours: 4 },
    // Add more initial Instructors as needed
  ]);

  const handleAddInstructor = () => {
    const newInstructor = { name: 'New Instructor', creditHours: 0 };
    setInstructors([...instructors, newInstructor]);
    setIsEditMode(true); // Automatically switch to edit mode for the newly added Instructor
  };

  const handleDeleteInstructor = (index) => {
    // Add your logic to handle deleting a Instructor
    const updatedInstructors = [...instructors];
    updatedInstructors.splice(index, 1);
    setInstructors(updatedInstructors);
  };

  const handleEditInstructor = (index, newName, newCreditHours) => {
    // Add your logic to handle editing a Instructor name and credit hours
    const updatedInstructors = [...instructors];
    updatedInstructors[index].name = newName;
    updatedInstructors[index].creditHours = newCreditHours;
    setInstructors(updatedInstructors);
  };

  return (
    <Accordion className="my-3">
      <AccordionSummary
        expandIcon={<ExpandMoreIcon />}
        aria-controls="panel1-content"
        id="panel1-header"
      >
        Instructors
      </AccordionSummary>
      <AccordionDetails>
        <div className="w-full">
          {instructors.map((instructor, index) => (
            <div key={index} className="flex items-center my-2">
              <TextField
                type="text"
                label="Instructor Name"
                value={instructor.name}
                onChange={(e) => handleEditInstructor(index, e.target.value, instructor.creditHours)}
                className="w-3/4"
              />
              <Button
                onClick={() => handleDeleteInstructor(index)}
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
        <Button onClick={handleAddInstructor}>
          Add
        </Button>
        <Button onClick={() => setIsEditMode(!isEditMode)}>
          {isEditMode ? 'Save' : 'Edit'}
        </Button>
      </AccordionActions>
    </Accordion>
  );
};
