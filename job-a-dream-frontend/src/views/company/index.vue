<script setup lang="ts">
import { storeToRefs } from 'pinia'
import { useCompanyStore } from '@/stores/companyStore'

const companyStore = useCompanyStore()
const { company } = storeToRefs(companyStore)
const route = useRoute()

onMounted(() => {
  if ('id' in route.params) {
    const id = route.params.id

    companyStore.getCompany(id)
  }
})
console.log('company', company.value)
</script>

<template>
  <VRow>
    <!-- 👉 Radar Chart -->
    <VCol cols="12">
      <VCard :title="company.name">
        <VCardText>
          {{ company.name }}
        </VCardText>
      </VCard>
    </VCol>
    <VCol cols="12" />
  </VRow>
</template>
