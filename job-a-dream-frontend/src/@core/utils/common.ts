import type { IconProp } from '../types'

export const isIconProp = (icon: any): icon is IconProp => {
  return icon === undefined || (typeof icon === 'object' && icon !== null)
}
export const getIconProps = (icon: any, defaultIconProps: any) => {
  if (isIconProp(icon))
    return icon

  return isIconProp(defaultIconProps) ? defaultIconProps : {}
}
