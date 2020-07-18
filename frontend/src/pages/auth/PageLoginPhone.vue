<template>
  <div class="q-pa-md row items-start q-gutter-md">
    <q-card :class="$q.platform.is.desktop ? 'absolute-center my-card q-pa-lg' : ''" flat>
      <q-card-section class="">
        <div class="text-overline text-orange-9"> Login or Create a New Account </div>
        <div class="text-h6 q-mt-sm q-mb-xs"> Enter your phone number </div>
        <div class="q-gutter-md row q-pa-md">
            <q-select dense transition-show="scale" transition-hide="scale" v-model="country_code" :options="['+91', '+1']" class="col-3">
                <template v-slot:prepend>
                    <q-avatar size="sm">
                        <img :src="country_code == '+91' ? 'india-flag.png' : 'usa-flag.png'">
                    </q-avatar>
                </template>
            </q-select>

            <q-input
                class="col"
                dense
                v-model="phone_number"
                placeholder="Phone number"
                :mask="country_code == '+91' ? '##### #####' : '(###) ### - ####'"
            />
        </div>
      </q-card-section>

      <q-card-actions>
        <q-space />
        <q-btn flat color="dark" label="Cancel" />
        <q-btn  color="primary" label="Verify" />
      </q-card-actions>

      <q-space />

      <q-card-section class="q-pt-xs">
        <div class="text-caption text-grey">
            By tapping Verify, an SMS may be sent. Message & data rates may apply.
        </div>
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
export default {
  data () {
    return {
      country_code: '+91',
      phone_number: null
    }
  }
}
</script>


<style lang="sass" scoped>
.my-card
  width: 100%
  max-width: 450px
</style>