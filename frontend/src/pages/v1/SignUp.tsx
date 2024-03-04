import React, {useState} from "react";
import { useLocation } from "react-router-dom";

const ErrorMessage = (errors: any)=>{

  if (!errors) {
    return null;
  }

  return (
    <div>
      <ul>
      {errors.map((error:any, index:number)=>{
        <li key={index} className="color-red-900">{error}</li>
      })}
      </ul>
    </div>
  )
}

const SignUp = () => {

  const [userName, setUserName] = useState<string>('');
  const [email, setEmail] = useState<string>('');
  const [isCreator, setIsCreator] = useState<string>('false');
  const [password, setPassword] = useState<string>('');
  const [password2, setPassword2] = useState<string>('');
  const [errors, setErrors] = useState(null);

  const location = useLocation();
  if (location.state.state === 'creator'){
    setIsCreator('true')
  }

  const baseUrl = 'http://localhost:8000/api_root/auth/signup/';

  const handleFetch = async (e:any) => {
    e.preventDefault();

    const formData = new FormData();
    formData.append('username', userName)
    formData.append('email', email)
    formData.append('is_creator', isCreator)
    formData.append('password',password)
    formData.append('password2', password2)


    const requestOptions = {
      method: 'POST',
      body: formData,
      // headers: {
      //           "Content-type": "multipart/form-data; charset=UTF-8"
      //       }
    };

    try {
      const response = await fetch(baseUrl, requestOptions);
      if (response.ok) {
        console.log('Data posted successfully');

      }else if (response.status === 400){
        const data =await response.json()

        if ('username' in data){
          setErrors(data['username'])
        }else if('email' in data){
          setErrors(data['email'])
        }else if('password' in data){
          console.log(data['password'])
        }
        // for (error in data){
        //   console.error(data.password)
        // }
        
      }
      else {
        console.error('Failed to post data');
      }
    } catch (error) {
      console.error('Error posting data:', error);
    }
      
  };

  return (
    <div className="h-[100vh] items-center flex justify-center px-5 lg:px-0">
      <div className="max-w-screen-xl bg-white border shadow sm:rounded-lg flex justify-center flex-1">
        <div className="flex-1 bg-blue-900 text-center hidden md:flex">
          <div
            className="m-12 xl:m-16 w-full bg-contain bg-center bg-no-repeat"
            style={{
              backgroundImage: `url(https://www.tailwindtap.com/assets/common/marketing.svg)`,
            }}
          ></div>
        </div>
        <div className="lg:w-1/2 xl:w-5/12 p-6 sm:p-12">
          <div className=" flex flex-col items-center">
            <div className="text-center">
              <h1 className="text-2xl xl:text-4xl font-extrabold text-blue-900">
                Sign up
              </h1>
              <p className="text-[12px] text-gray-500">
                Hey enter your details to create your account
              </p>
            </div>
            <form className="w-full flex-1 mt-8" onSubmit={handleFetch}>
              <div className="mx-auto max-w-xs flex flex-col gap-4">
                <input
                  className="w-full px-5 py-3 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white"
                  type="text"
                  onChange={(e)=>setUserName(e.target.value)}
                  placeholder="Enter your name"
                  required
                />
                <input
                  className="w-full px-5 py-3 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white"
                  type="email"
                  onChange={(e)=>setEmail(e.target.value)}
                  placeholder="Enter your email"
                  required
                />
                <input
                  className="w-full px-5 py-3 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white"
                  type="password"
                  onChange={(e)=>setPassword(e.target.value)}
                  placeholder="Password"
                  required
                />
                <input
                  className="w-full px-5 py-3 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white"
                  type="password"
                  onChange={(e)=>setPassword2(e.target.value)}
                  placeholder="Confirm Password"
                  required
                />
                {/* <ErrorMessage errors={errors}/> */}
                <button 
                  type='submit'
                  className="mt-5 tracking-wide font-semibold bg-blue-900 text-gray-100 w-full py-4 rounded-lg hover:bg-indigo-700 transition-all duration-300 ease-in-out flex items-center justify-center focus:shadow-outline focus:outline-none">
                  <svg
                    className="w-6 h-6 -ml-2"
                    fill="none"
                    stroke="currentColor"
                    strokeWidth="2"
                    strokeLinecap="round"
                    strokeLinejoin="round"
                  >
                    <path d="M16 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2" />
                    <circle cx="8.5" cy="7" r="4" />
                    <path d="M20 8v6M23 11h-6" />
                  </svg>
                  <span className="ml-3">Sign Up</span>
                </button>
                <p className="mt-6 text-xs text-gray-600 text-center">
                  Already have an account?{" "}
                  <a href="/login">
                    <span className="text-blue-900 font-semibold">Sign in</span>
                  </a>
                </p>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
};
export default SignUp;
