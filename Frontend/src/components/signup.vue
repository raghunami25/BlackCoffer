<template>
  <v-app id="inspire"  style="background-image: linear-gradient(to top, #30cfd0 0%, #330867 100%);">
    <v-content>
      <v-container fluid fill-height>
        <v-row
          align="center"
          justify="center"
        >
          <v-col
            cols="12"
            sm="8"
            md="4"
          >
            <v-card class="elevation-25" height="100%" overflow-y=auto;>
              <v-toolbar
                color="primary"
                dark
                flat
              >
               <v-toolbar-title>Register</v-toolbar-title>
            </v-toolbar>
               
              <v-card-text>
                <v-form>
                  <v-text-field
                    label="username"
                    v-model="user"
                    prepend-icon="person"
                    type="text"
                  ></v-text-field>

                  <v-text-field
                    id="password"
                    label="Password"
                    v-model="password"
                    prepend-icon="lock"
                    type="password"
                  ></v-text-field>
                  <v-text-field
                    id="password"
                    label="Confirm Password"
                    v-model="password"
                    prepend-icon="lock"
                    type="password"
                  ></v-text-field>
                </v-form>
              </v-card-text>
              <v-card-actions>
                <div class="flex-grow-1"></div>
                <v-btn color="primary"  @click="Signup()">Sign Up</v-btn>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
        <div id="sign"></div>
      </v-container>
    </v-content>
  </v-app>
</template>
<script>
  export default {
    props: {
      source: String,
    },


    data: () => ({
      drawer: null,
    }),
    methods: {

      Signup(){
        const dat = {
          username : this.user,
          password : this.password
        };
        this.$http.post('http://localhost:5000/sign_up', dat,{
          headers: {
            'Content-Type': 'application/json'
          }}).then((resp)=>{
            res = resp.data
            if(res == "inserted"){
              document.getElementById('sign').innerHTML = "Register Successfully";
            }
        });
      },
      
    },
  }
</script>