document.addEventListener('DOMContentLoaded', function(){
    document.getElementById('submit').addEventListener('submit', function(event){
        event.preventDefault();

        var username = document.getElementById('username').value;
        var password = document.getElementById('password').value;

        axios.post('http://localhost:8000/auth/register/',{
            username:username,
            password:password,
        }).then(function(response){
            console.log(response.data);
            alert('Registration Successful');
        })
        .catch(function(error){
            console.log(error);
            alert('Registration Failed');
        });

    });
});