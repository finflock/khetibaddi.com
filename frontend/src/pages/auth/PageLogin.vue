<template>
  <div class="q-pa-md row items-start q-gutter-md">
    <q-card :class="$q.platform.is.desktop ? 'absolute-center my-card q-pa-lg' : 'q-mt-xl'" flat>
      <q-card-section>
        <div class="text-overline text-orange-9"> Login or Create a New Account </div>
        <div class="text-h6 q-mt-sm q-mb-xs"> Enter your email and password </div>
        <div class="q-gutter-md q-pa-md">
            <q-input dense filled v-model="formData.email" type="email" label="Email">
              <template v-slot:prepend>
                    <q-icon name="email" class="on-left" />
                </template>
            </q-input>

            <q-input bottom-slots dense filled v-model="formData.password" :type="isPwd ? 'password' : 'text'" placeholder="Password">
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
                <template v-slot:hint>
                    <span class="float-right"> Forgot password? </span>
                </template>
            </q-input>
        </div>
      </q-card-section>

      <q-card-actions>
        <q-space />
        <!-- <q-btn flat color="dark" label="Cancel" /> -->
        <q-btn icon="lock_open" class="q-mx-lg" style="width:100%" color="primary" label="Login Securely" @click="submitForm" />
        <!-- <q-space /> -->
      </q-card-actions>

      <q-space />

      <q-card-section class="q-pt-lg">
        <div class="text-caption text-grey">
            <span> Don't have an account ? </span>
            <q-btn flat no-caps size="13px" align="left" color="light-blue" class="q-mb-xs btn-fixed-width" label="Click here." to="/auth-register" />
        </div>
        <div class="text-caption text-grey"> By proceeding, you agree to our Terms & Conditions and Privacy Policy. </div>
    </q-card-section>

    <q-card-actions>
        <q-space />
        <q-btn flat no-caps size="13px" color="info" label="Terms of Service" />
        <q-btn flat no-caps size="13px" color="info" label="Privacy Policy" />
    </q-card-actions>

    </q-card>

  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  data () {
    return {
        formData: {
            email: '',
            password: ''
        },
        isPwd: true
    }
  },
  methods: {
    ...mapActions('store', ['loginUser']),
    submitForm() {
      this.loginUser(this.formData)
    }
  },
}
</script>


<style lang="scss">

  .header-image {
    height: 100%;
    z-index: -1;
    opacity: 0.4;
    // filter: grayscale(40%)
  }
</style>

