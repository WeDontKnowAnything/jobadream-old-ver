<script lang="ts" setup>
import type { GridColumn } from '@core/types'

interface Props {
  selectedCheckbox: string[]
  checkboxContent: string[]
  gridColumn?: GridColumn
}

interface Emit {
  (e: 'update:selectedCheckbox', value: string[]): void
}

const props = defineProps<Props>()
const emit = defineEmits<Emit>()

const updateSelectedOption = (value: string[] | boolean) => {
  if (typeof value !== 'boolean')
    emit('update:selectedCheckbox', value)
}
</script>

<template>
  <VRow v-if="props.checkboxContent && props.selectedCheckbox">
    <VCol
      v-for="item in props.checkboxContent"
      :key="item"
      v-bind="gridColumn"
    >
      <VLabel
        class="custom-input custom-checkbox rounded cursor-pointer"
        :class="props.selectedCheckbox.includes(item) ? 'active' : ''"
      >
        <div>
          <VCheckbox
            :model-value="props.selectedCheckbox"
            :value="item"
            @update:model-value="updateSelectedOption"
          />
        </div>
        <slot :item="item">
          <div class="flex-grow-1">
            <div class="d-flex align-center">
              <h6 class="cr-title text-base">
                {{ item }}
              </h6>
            </div>
          </div>
        </slot>
      </VLabel>
    </VCol>
  </VRow>
</template>

<style lang="scss" scoped>
.custom-checkbox {
  .cr-title {
    font-weight: 500;
  }
}
</style>
