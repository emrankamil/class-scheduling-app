// import Accordion from '@mui/material/Accordion';
// import AccordionDetails from '@mui/material/AccordionDetails';
// import AccordionSummary from '@mui/material/AccordionSummary';
// import Typography from '@mui/material/Typography';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';




import React, { useState } from 'react';
import { Accordion, AccordionSummary, AccordionDetails, TextField, Typography, FormLabel, FormControlLabel, Checkbox, Divider, AccordionActions, Button } from '@mui/material/';
import { FormControl, FormGroup, Grid, IconButton } from '@mui/material';
import { Add as AddIcon, Remove as RemoveIcon } from '@mui/icons-material';
// import Button from '../../Controls/Button';
import { ContactSupportOutlined } from '@mui/icons-material';
import useStyles from './styles';



export default function Department() {
  const [expanded, setExpanded] = React.useState<string | false>(false);

  const handleChange1 =
    (panel: string) => (event: React.SyntheticEvent, isExpanded: boolean) => {
      setExpanded(isExpanded ? panel : false);
    };

    const [state, setState] = useState({
        monday: true,
        tuesday: false,
        wensday: false,
        thrusday: false,
        friday: false,
    });
    const [time, settime] = useState({
        m1: true,
        m2: false,
        m3: false,
        m4: false,
        m5: false,
        m6: false,
        m7: false
    })
    const { monday, tuesday, wensday, thrusday, friday } = state;
    const { m1, m2, m3, m4, m5, m6, m7 } = time;

    const [departementName, setDepartementName] = useState('')
    // Values of Inputs
    const [courseFields, setcourseFields] = useState([
        { courseName: '', creditHour: '', courseInstactor: '' }
    ])
    const [classRoomFields, setclassRoomFields] = useState([
        { roomName: '', roomCapacity: '' }
    ])
    const [noOfStudent, setnoOfStudent] = useState(0);

    const handleRoomClick = () => {
        // console.log("sjdkf")
        const values = [...classRoomFields];
        values.push({ roomName: '', roomCapacity: '' });
        setclassRoomFields(values);
        console.log(courseFields.length);
    }
    const handleCourseRemoveClick = (i:any) => {
        console.log(i)
    }
    const handleCourseClick = () => {
        // console.log("sjdkf")
        const values = [...courseFields];
        values.push({ courseName: '', creditHour: '', courseInstactor: '' });
        setcourseFields(values);
        console.log(courseFields.length);
    }
    const handleRoomRemoveClick = (i:any) => {
        console.log(i)
    }
    const handleInputChange = (index:any, event:any) => {
        const courseValue = [...courseFields];
        const classRoomValue = [...classRoomFields];
        if (event.target.name === "courseName") {
            courseValue[index].courseName = event.target.value;
        } else if (event.target.name === "courseCreditHour") {
            courseValue[index].creditHour = event.target.value;
        } else if (event.target.name === "courseInstactor") {
            courseValue[index].courseInstactor = event.target.value;
        } else if (event.target.name === "roomName") {
            classRoomValue[index].roomName = event.target.value;
        } else if (event.target.name === "roomCapacity") {
            classRoomValue[index].roomCapacity = event.target.value;
        }

        setcourseFields(courseValue);
        setclassRoomFields(classRoomValue);
    };
    const resetForm = () => {
        setclassRoomFields([{ roomName: '', roomCapacity: '' }]);
        setcourseFields([{ courseName: '', creditHour: '', courseInstactor: '' }]);
        setDepartementName('')
        setnoOfStudent(0)
    }

    const handleSingleItemChange = (e:any) => {
        if (e.target.name === "Departement") {
            // console.log(e.target.value);
            setDepartementName(e.target.value)
        } else if (e.target.name === "totalStudent") {
            setnoOfStudent(e.target.value)
        }

    }


    // const handleSave = () => {
    //     handleMessage(initalValue, index - 1);
    //     console.log(state);
    // }
    const handleChange = (event:any) => {
        setState({ ...state, [event.target.name]: event.target.checked });
    };
    const handletimeChange = (event:any) => {
        settime({ ...time, [event.target.name]: event.target.checked });
    };

    const initalValue = {
        departementName: departementName,
        course: courseFields,
        classRoom: classRoomFields,
        noOfStudent: noOfStudent,
        days: state,
        time: time
    }

  return (
    <div>
      <Accordion expanded={expanded === 'panel1'} onChange={handleChange1('panel1')}>
        <AccordionSummary
          expandIcon={<ExpandMoreIcon />}
          aria-controls="panel1bh-content"
          id="panel1bh-header"
        >
            place holder
        </AccordionSummary>
        <AccordionDetails>
            <Typography>
                Department
            </Typography>
        <div className='flex'>
            <form className="max-w-sm mx-auto">
                <label htmlFor="countries" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Select your country</label>
                <select id="countries" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">

                    <option>United States</option>
                    <option>Canada</option>
                    <option>France</option>
                    <option>Germany</option>
                </select>
            </form>



            <fieldset>
                <legend className="sr-only">Checkbox variants</legend>

                <div className="flex items-center mb-4">
                    <input checked id="checkbox-1" type="checkbox" value="" className="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600" ></input>
                    <label htmlFor="checkbox-1" className="ms-2 text-sm font-medium text-gray-900 dark:text-gray-300">I agree to the <a href="#" className="text-blue-600 hover:underline dark:text-blue-500">terms and conditions</a>.</label>
                </div>

                <div className="flex items-center mb-4">
                    <input id="checkbox-2" type="checkbox" value="" className="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600"></input>
                    <label htmlFor="checkbox-2" className="ms-2 text-sm font-medium text-gray-900 dark:text-gray-300">I want to get promotional offers</label>
                </div>

                <div className="flex items-center mb-4">
                    <input id="checkbox-3" type="checkbox" value="" className="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600"></input>
                    <label htmlFor="checkbox-3" className="ms-2 text-sm font-medium text-gray-900 dark:text-gray-300">I am 18 years or older</label>
                </div>
                
                <div className="flex mb-4">
                    <div className="flex items-center h-5">
                        <input id="helper-checkbox" aria-describedby="helper-checkbox-text" type="checkbox" value="" className="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600"></input>
                    </div>
                    <div className="ms-2 text-sm">
                        <label htmlFor="helper-checkbox" className="font-medium text-gray-900 dark:text-gray-300">Free shipping via Flowbite</label>
                        <p id="helper-checkbox-text" className="text-xs font-normal text-gray-500 dark:text-gray-400">For orders shipped from $25 in books or $29 in other categories</p>
                    </div>
                </div>

                <div className="flex items-center">
                    <input id="international-shipping-disabled" type="checkbox" value="" className="w-4 h-4 border-gray-300 rounded bg-gray-50 focus:ring-3 focus:ring-blue-300 dark:bg-gray-700 dark:border-gray-600 dark:focus:ring-blue-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800" disabled></input>
                    <label htmlFor="international-shipping-disabled" className="ms-2 text-sm font-medium text-gray-400 dark:text-gray-500">Eligible for international shipping (disabled)</label>
                </div>
            </fieldset>
        </div>
        </AccordionDetails>
      </Accordion>
      
      
        <Divider />
        <AccordionActions>
        <Button size="small" onClick={resetForm}>Reset</Button>
        <Button size="small" color="primary" >
            Save
        </Button>
        </AccordionActions>
        </div>
  );
}