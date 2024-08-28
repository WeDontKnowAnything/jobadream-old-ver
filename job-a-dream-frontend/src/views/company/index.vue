<script setup lang="ts">
import { storeToRefs } from 'pinia'
import { useCompanyStore } from '@/stores/companyStore'

const companyStore = useCompanyStore()
const { company } = storeToRefs(companyStore)
const route = useRoute()

onMounted(() => {
  const id = route.params.id

  console.log('id', id)
  companyStore.getCompany(id)
})
console.log('company', company.value)
</script>

<template>
  <VRow>
    <!-- 👉 Radar Chart -->
    <VCol
      cols="12"
      md="6"
    >
      <VCard :title="company.name">
        <VCardText>
          {{ company.name }}
        </VCardText>
      </VCard>
    </VCol>
  </VRow>
</template>
