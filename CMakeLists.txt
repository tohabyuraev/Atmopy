# Указание на необходимую версию CMake
cmake_minimum_required(VERSION 3.19)

# Название проекта
project(atmopy VERSION 0.1)

# Команды для компилятора
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_FLAGS "-Wall")

# Указание на библиотеку
set(ATMOPY "atmopy")

set(CORE ${ATMOPY}/core)
set(SOURCE ${ATMOPY}/source)

# Информация про DLL
set(SOURCE_RC info.rc)

# Расположение заголовочных файлов
include_directories(${CORE}/ ${SOURCE}/)

# Установка переменной со списком исходников
set(SOURCE_LIB
    ${CORE}/interp.cpp)

# Создание библиотеки с именем lebedev
# add_library(${PROJECT_NAME} STATIC ${SOURCE_LIB})
# add_library(${PROJECT_NAME} SHARED ${SOURCE_LIB})

add_library(${PROJECT_NAME} SHARED ${SOURCE_LIB} ${SOURCE_RC})