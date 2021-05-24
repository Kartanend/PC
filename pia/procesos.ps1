# Obtiene los procesos del sistema y los convierte en formato de tabla.
#
# Returns:
#   Un objeto que contiene los procesos del sistema.

$proc = get-process | Format-Table
return $proc