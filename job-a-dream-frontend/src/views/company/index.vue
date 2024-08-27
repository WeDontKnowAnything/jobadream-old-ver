<script setup lang="ts">
import { storeToRefs } from 'pinia'
import { useCompanyStore } from '@/stores/companyStore'

const companyStore = useCompanyStore()
const { company } = storeToRefs(companyStore)
</script>

<template>
  <VRow id="chartjs-wrapper">
    <!-- 👉 Radar Chart -->
    <VCol
      cols="12"
      md="6"
    >
      <VCard :title="company.corp_name">
        <VCardText>
          {{ company.corp_name }}
        </VCardText>
      </VCard>
    </VCol>
  </VRow>
</template>
