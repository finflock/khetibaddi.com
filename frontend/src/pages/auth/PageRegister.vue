<template>
  <div class="q-pa-md row items-start q-gutter-md">
    <q-card :class="$q.platform.is.desktop ? 'absolute-center my-card q-pa-lg' : ''" flat style="width:100%">

        <i class="ml-1 flag-icon flag-icon-us h5" title="USA" id="us"></i> 

      <q-card-section>
        <div class="text-overline text-orange-9"> Creating a New Account </div>
        <div class="text-h6 q-mt-sm q-mb-xs"> Enter your account details </div>
        <!-- {{commoditySeller}}
        {{commodityBuyer}}
        {{commodityTransporter}} -->

        <div class="q-gutter-md  q-pa-sm">
            <q-input filled dense v-model="formData.name" type="text" placeholder="Name">
              <template v-slot:prepend>
                    <q-icon name="person" class="on-left" />
                </template>
            </q-input>

            <q-select filled dense v-model="formData.gender" label="Select your gender" :options="['Male', 'Female']"> 
              <template v-slot:prepend>
                    <q-icon name="person" class="on-left" />
                </template>
            </q-select>

            <q-input filled dense v-model="formData.phone_no" type="text" placeholder="Phone number">
              <template v-slot:prepend>
                    <q-icon name="call" class="on-left" />
                </template>
            </q-input>

            <q-input filled dense v-model="formData.email" type="email" placeholder="Email">
              <template v-slot:prepend>
                    <q-icon name="email" class="on-left" />
                </template>
            </q-input>

            <q-select filled dense v-model="formData.user_type" label="Select a user type" :options="['Commodity Seller', 'Commodity Transporter', 'Commodity Buyer']"> 
              <template v-slot:prepend>
                    <q-icon name="person" class="on-left" />
                </template>
            </q-select>

            <q-input filled dense v-model="formData.password" :type="isPwd ? 'password' : 'text'" placeholder="Password">
              <template v-slot:prepend>
                    <q-icon name="vpn_key" class="on-left" />
              </template>
              <template v-slot:append>
                  <q-icon
                      :name="isPwd ? 'visibility_off' : 'visibility'"
                      class="cursor-pointer"
                      @click="isPwd = !isPwd"
                  />
              </template>
            </q-input>
        </div>
      </q-card-section>

      <q-card-actions>
        <!-- <q-space /> -->
        <q-btn icon="backspace" class="col" outline color="orange-9" label="Cancel" to="/auth-login"/>
        <q-btn icon="person_add" class="col" color="primary" label="Create" @click="submitForm"/>
      </q-card-actions>

      <q-space />

      <!-- <q-card-section class="q-pt-xs">
        <div class="text-caption text-grey">
            By tapping Create, you are agreeing to the terms and conditions.
        </div>
    </q-card-section> -->

    <q-card-actions>
        <q-space />
        <q-btn flat no-caps size="13px" color="info" label="Terms of Service"/>
        <q-btn flat no-caps size="13px" color="info" label="Privacy Policy" />
    </q-card-actions>

    </q-card>
  </div>
</template>

<script>
import axios from 'axios';
import { mapActions } from 'vuex'
// import { mapGetters } from 'vuex'
  
export default {
  data () {
    return {
      api_url: "http://www.khetibaddi.com/api/v1/",
      val: true,
      country_code: '+91',
      formData: {
          name: '',
					phone_no: '',
          email: '',
          user_type: '',
          password: '',
          gender: ''
        },
      isPwd: true        
    }
  },

  computed: {
    commoditySeller() {
      if(this.formData.user_type == 'Commodity Seller' ) return true
      else return false
    },
    commodityBuyer() {
      if(this.formData.user_type == 'Commodity Buyer' ) return true
      else return false
    },
    commodityTransporter() {
      if(this.formData.user_type == 'Commodity Transporter' ) return true
      else return false
    },
  },
  
  methods: {
    ...mapActions('store', ['registerUser', 'loginUser']),
    submitForm() {
      this.registerUser(this.formData)
      this.postUser()
    },

    postUser() {
      const params = new URLSearchParams();
      params.append('full_name', this.formData.name);
      params.append('email', this.formData.email);
      params.append('mobile', this.formData.phone_no);
      params.append('gender', this.formData.gender);
      params.append('password', this.formData.password);
      params.append('commodity_seller', this.commoditySeller);
      params.append('commodity_buyer', this.commodityBuyer);
      params.append('commodity_transport_provider', this.commodityTransporter);
      params.append('is_active', true);

      axios.post(this.api_url+'users/', params)
          .then(response => {
              console.log("User Registered")
          })
          .catch(e => {
              console.log("Error while registeration")              
          });
    }
  },
    
}
</script>

<style lang="sass" scoped>
.my-card
  width: 100%
  max-width: 450px
</style>