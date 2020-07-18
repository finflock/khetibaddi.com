<template>
  <div>
    <!-- {{getUserDetails.user_type}} -->
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  data() {
    return {
      
    }
  },

  computed: {
      ...mapGetters('store', ['getUserDetails'])
  },

  methods: {
      loadDashboard() {
	  		setTimeout(() => {
		  		if(this.getUserDetails) {
              if(this.getUserDetails.user_type == 'Commodity Seller') {
                this.$router.push('/seller-dashboard')
              } else if(this.getUserDetails.user_type == 'Commodity Buyer'){
                this.$router.push('/buyer-dashboard')
              } else {
                this.$router.push('/transporter-dashboard')
              }
          }
	  		}, 2000);
	  	}
  },

  created() {
    this.loadDashboard();
    // if(this.getUserDetails.user_type) {
    //     if(this.getUserDetails.user_type == 'Commodity Seller') {
    //       this.$router.push('/seller-dashboard')
    //     } else if(this.getUserDetails.user_type == 'Commodity Buyer'){
    //       this.$router.push('/buyer-dashboard')
    //     } else {
    //       this.$router.push('/transporter-dashboard')
    //     }
    // }
  }
}
</script>

<style>

</style>
