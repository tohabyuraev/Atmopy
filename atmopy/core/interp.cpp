#include "interp.hpp"


float interp(
    const float x,
    const Line* l)
{
    vector_t data_x_ = vector_t(l->x, l->x + l->n);
    vector_t data_y_ = vector_t(l->y, l->y + l->n);
    return interp1d(x, data_x_, data_y_);
}
float interp1d(
    const float x,
    const vector_t& data_x,
    const vector_t& data_y)
{
    auto bound = std::equal_range(
        data_x.begin(), data_x.end(), x);

    if (data_x.begin() == bound.first) {
        return data_y.front();
    } else if (data_x.end() == bound.second) {
        return data_y.back();
    } else {
        const int i = bound.first - data_x.begin() - 1;
        const int j = bound.first - data_x.begin() - 0;

        return data_y[j] + (x - data_x[j]) *
            (data_y[i] - data_y[j]) /
            (data_x[i] - data_x[j]);
    };
}
