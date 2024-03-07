import React from 'react';
import { Link } from 'react-router-dom'; 

const Navbar: React.FC = () => {
  return (
      <nav className="flex justify-right bg-gray-800 p-2 gap-2 w-full ">
        <Link to="/" className="text-white font-bold border-2 rounded-lg">Logo</Link>
        <Link to="/v1" className="text-white border-2 rounded-lg">New Schedule</Link>
        <Link to="/class" className="text-white border-2 rounded-lg">Shecdule Class</Link>
        <Link to="/exam" className="text-white border-2 rounded-lg">Shecdule Exam</Link>
            
        </nav>
  );
};

export default Navbar;


// const LandingPage = () => {
//   return (
//     <div className="flex h-screen gap-2 p-2 bg-black">
      

//       {/* Right side */}
//       <div className="flex-1 flex flex-col bg-green-500 rounded-r-lg">

//         <nav className="bg-gray-800 text-white p-4">
//           <div className="container mx-auto flex justify-between items-center">
//             <Link to="/" className="text-lg font-semibold">
//               Home
//             </Link>
//             <div className="" id='search'>
//               <input type="text" placeholder="Search..." className="p-2 rounded-md border-2 bg-transparent text-gray-800" />
//             </div>
//             <div className="flex space-x-4">
//               <Link to="/login">Login</Link>
//               <Link to="/signup">sign up</Link>
//             </div>
//           </div>
//         </nav>
//       </div>
//     </div>
//   );
// };

