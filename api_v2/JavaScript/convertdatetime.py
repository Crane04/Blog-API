def convert_datetime():
    convert_datetime_function = """
        function convert_datetime(param){
        try{
        
            const dateComponents = param.match(/(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):(\d{2})/);

            const year = parseInt(dateComponents[1]);
            const month = parseInt(dateComponents[2]) - 1;
            const day = parseInt(dateComponents[3]);

            // Create a JavaScript Date object without considering the timezone
            const date = new Date(year, month, day);

            const time = new Date(param);

            // Get the hours, minutes, and seconds
            const hours = time.getHours();
            const minutes = time.getMinutes();
            const seconds = time.getSeconds();

            let __time__ = `${hours}:${minutes}:${seconds}`;

            // Format the date as "Month Day, Year"
            return   date.toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' }).toString() + " ; " + __time__;
        }catch(error){
            return param
        }

        }
"""
    return convert_datetime_function

