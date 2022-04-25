#ifndef _INTERP_H_
#define _INTERP_H_

#include <iostream>
#include <vector>
#include <algorithm>


using vector_t = std::vector<float>;

struct Line
{
    float* x;
    float* y;
    size_t n;
};

#ifdef  __cplusplus
extern "C" {
#endif

float interp(
    const float,
    const Line*);
float interp1d(
    const float,
    const vector_t&,
    const vector_t&);

#ifdef  __cplusplus
}
#endif

#endif  /* _INTERP_H_ */
