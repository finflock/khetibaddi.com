<template>
  <div class="q-pa-md" style="max-width: 350px">
    <q-list>
      <div v-for="assignment in assignments" :key="assignment.id">
          <q-item clickable v-ripple >
            <q-item-section>
                <q-item-label class="text-bold text-brown-9" lines="1"> {{assignment.commodity_name}} </q-item-label>
                <q-item-label caption lines="1" class="text-bold"> Expected by </q-item-label>
                <q-item-label caption lines="1"> <span class="text-"> {{assignment.expected_date}} </span> </q-item-label>
            </q-item-section>

            <q-item-section side bottom class="q-mt-sm">
                <q-item-label caption> <span class="text-bold text-light-blue-7"> ₹ {{assignment.price}} </span> <span class="text-bold text-grey-7">for {{assignment.quantity}} Quintal </span> </q-item-label>
                <!-- <q-badge :class="listing.status == 'Open' ? 'q-mt-sm q-px-sm q-py-xs text-positive' : 'q-mt-sm q-px-sm q-py-xs text-red-12'" :color="listing.status == 'Open' ? 'green-1' : 'red-1'"> -->
                <q-badge class="q-mt-sm q-px-sm q-py-xs text-light-blue" color="cyan-1">
                <span class="text-uppercase text-bold"> {{assignment.status}} </span> 
                </q-badge>
            </q-item-section>
            </q-item>

        <q-separator spaced inset />
      </div>
    </q-list>
  </div>
</template>

<script>
export default {
    data() {
        return {
            assignments: [{
                id: 1,
                commodity_name: 'Red Chilli',
                price: '7,500',
                quantity: 70,
                status: 'Pending',
                expected_date: '19 July, 9:30 am'
            },
            {
                id: 2,
                commodity_name: 'Mangoes',
                price: '13,500',
                quantity: 50,
                status: 'Pending',
                expected_date: '21 July, 11:30 am'
            }]
        }
    }
}
</script>
