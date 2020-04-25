### Standardization (z-score Normalization)

$$
x' = \frac{x - μ}{σ}
$$

### Normalization (L2 Normalization)

$$
x_i' = \frac{x_i}{\sqrt{\sum_{i=1}^{n}{x_i^2}}}
$$

$x_i' = \frac{x_i}{\sqrt{\sum_{i=1}^{n}{x_i^2}}}$

```ruby
L2({"a" => 1, "b" => -1}) = {"a" => 0.707, "b" => -0.707}
L2({"a" => 2, "b" => -2}) = {"a" => 0.707, "b" => -0.707}
```

$$
\frac{1}{\sqrt{1^2 + (-1)^2}} = \frac{2}{2\sqrt{2}} = \frac{2}{\sqrt{2^2 + (-2)^2}}
$$

### Regularization

$$
L(w,X) = \frac{\lambda}{2} \left\lVert w \right\rVert ^ 2 + \frac{1}{n} \sum_{i} \frac{1}{2} \left(f(w,x_i) - y_i\right) ^ 2
$$

