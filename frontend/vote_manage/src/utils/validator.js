// 策略
const Strategies = {
  isNonEmpty(value, errorMsg) {
    if (value === "") return errorMsg;
  },
  minLength(value, errorMsg, min) {
    if (value.length < min) return errorMsg;
  },
  checkEmailFormat(value, errorMsg) {
    let pattern =
      /^[A-Za-z0-9-_\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$/;
    if (!pattern.test(value)) return errorMsg;
  },
  codeLength(value, errorMsg) {
    return value.length == 4 ? errorMsg : undefined;
  },
  comparePsd(value, errorMsg) {
    return value[0] !== value[1] ? errorMsg : undefined;
  },
  maxLength(value, errorMsg, max) {
    if (value.length > max) return errorMsg;
  },
  isNumber(value, errorMsg) {
    if (value !== "1" && value !== "0") return errorMsg;
  },
};

// 验证器
export class Validator {
  constructor() {
    this.cache = [];
  }

  add(dom, rule, errorMsg, min = 0) {
    this.cache.push(() => {
      return Strategies[rule](dom, errorMsg, min);
    });
  }

  start() {
    for (let i = 0; i < this.cache.length; i++) {
      let error = this.cache[i]();
      if (error) {
        return error;
        break;
      }
    }
  }
}
