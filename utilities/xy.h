#ifndef UTILITIES_XY_H
#define UTILITIES_XY_H

template <typename T> struct XY {
    XY() = default;
    XY(T _x, T _y) : x{_x}, y{_y} {}
    
    XY& operator+=(const XY& other) {
        x += other.x;
        y += other.y;
        return *this;
    }

    T x{0};
    T y{0};
};

#endif
