# LAB_DJNAGO_ORM_3_RELATIONS


## Create a Clinic Website , the clinic has the following :
- Home page to display all the doctors in your clinic .
- detail page for doctor, when clicked the doctor detail page is displayed.
- search page for doctors by name.


### A patient can do the following:
- Browse the doctors and view the doctor's detail page.
- View the previous appointments on the doctor's page.
- Book an appointment with a date on that doctor.


### Models

- Doctor model should have
- - name
- - description
- - specialization (use text choices)
- - experience_years
- - rating



- Appointment Model
- - Relation with doctor
- - patient_name
- - case_description
- - patient_age
- - appointment_datetime
- - is_attended


### styling
- Use bootstrap CSS library or similar for styling the website . 
- Use some images to represent the clinic building and facilities as a gallery.


### Bonus
When patient books an appointmnet with the doctor , check if the doctor is free on that date & time.








{% extends "clinicApp/clinic.html" %}

{% block home %}
{%endblock%}


{% block pu %}





<div class="container pt-4">
    <h1>Appointment :</h1>
   



   


    {% for app in appo_post %}


        <div class="col ">
          <div class="card ">
            <div class="card-body ">
                <br>
              <h3 class="card-title tex_co"> {{ app.patient_name }}</h3>
              <br>
              <h3 class="tex_co2">Age : {{ app.patient_age }}</h3>
    <div class="pt-2 text-center tex_co">
        {{ app.case_description }}
    </div>

       

              

              
            </div>

            
          </div>



     <hr>
        

        {% endfor %}




      </div>



    </div>

  




{% endblock %}






      <div class="pt-2">
        <select name="specialization" class="form-select" aria-label="Default select example">
          <option selected>your specialization ? </option>
          <option value="O">orthodontics</option>
          <option value="F">fillings</option>
          <option value="Or">oral medicine</option>
        </select> 
        </div>
