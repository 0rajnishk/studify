window.onload = function () {
  Particles.init({
    selector: ".background"
  });
};

const particles = Particles.init({
  selector: ".background",
  color: {
    value: ['#1abc9c', '#16a085', '#2ecc71', '#27ae60'],
  },
  connectParticles: false,
  size: {
    value: 2,
    random: true
  },
  move: {
    speed: 1
  },
  number: {
    density: {
      enable: true,
      value_area: 500
    },
    value: 200
  },
  opacity: {
    anim: {
      enable: true,
      opacity_min: 0.1,
      speed: 1,
      sync: false
    },
    random: true,
    value: 0.5
  },
  shape: {
    type: "circle",
    stroke: {
      width: 0,
      color: "#ffffff"
    },
    polygon: {
      nb_sides: 5
    },
  },
  responsive: [
    {
      breakpoint: 768,
      options: {
        color: {
          value: ['#1abc9c', '#16a085', '#2ecc71', '#27ae60'],
        },
        size: {
          value: 1,
          random: true
        },
        move: {
          speed: 0.5
        },
        number: {
          value: 100
        }
      }
    },
    {
      breakpoint: 425,
      options: {
        color: {
          value: ['#1abc9c', '#16a085', '#2ecc71', '#27ae60'],
        },
        size: {
          value: 1,
          random: true
        },
        move: {
          speed: 0.3
        },
        number: {
          value: 50
        }
      }
    }
  ]
});



class NavigationPage {
  constructor() {
    this.currentId = null;
    this.currentTab = null;
    this.tabContainerHeight = 70;
    this.lastScroll = 0;
    let self = this;
    $(".nav-tab").click(function () {
      self.onTabClick(event, $(this));
    });
    $(window).scroll(() => {
      this.onScroll();
    });
    $(window).resize(() => {
      this.onResize();
    });
  }

  onTabClick(event, element) {
    event.preventDefault();
    let scrollTop =
      $(element.attr("href")).offset().top - this.tabContainerHeight + 1;
    $("html, body").animate({ scrollTop: scrollTop }, 600);
  }

  onScroll() {
    this.checkHeaderPosition();
    this.findCurrentTabSelector();
    this.lastScroll = $(window).scrollTop();
  }

  onResize() {
    if (this.currentId) {
      this.setSliderCss();
    }
  }

  checkHeaderPosition() {
    const headerHeight = 600;
    if ($(window).scrollTop() > headerHeight) {
      $(".nav-container").addClass("nav-container--scrolled");
    } else {
      $(".nav-container").removeClass("nav-container--scrolled");
    }
    let offset =
      $(".nav").offset().top +
      $(".nav").height() -
      this.tabContainerHeight -
      headerHeight;
    if (
      $(window).scrollTop() > this.lastScroll &&
      $(window).scrollTop() > offset
    ) {
      $(".nav-container").addClass("nav-container--move-up");
      $(".nav-container").removeClass("nav-container--top-first");
      $(".nav-container").addClass("nav-container--top-second");
    } else if (
      $(window).scrollTop() < this.lastScroll &&
      $(window).scrollTop() > offset
    ) {
      $(".nav-container").removeClass("nav-container--move-up");
      $(".nav-container").removeClass("nav-container--top-second");
      $(".nav-container-container").addClass("nav-container--top-first");
    } else {
      $(".nav-container").removeClass("nav-container--move-up");
      $(".nav-container").removeClass("nav-container--top-first");
      $(".nav-container").removeClass("nav-container--top-second");
    }
  }

  findCurrentTabSelector(element) {
    let newCurrentId;
    let newCurrentTab;
    let self = this;
    $(".nav-tab").each(function () {
      let id = $(this).attr("href");
      let offsetTop = $(id).offset().top - self.tabContainerHeight;
      let offsetBottom =
        $(id).offset().top + $(id).height() - self.tabContainerHeight;
      if (
        $(window).scrollTop() > offsetTop &&
        $(window).scrollTop() < offsetBottom
      ) {
        newCurrentId = id;
        newCurrentTab = $(this);
      }
    });
    if (this.currentId != newCurrentId || this.currentId === null) {
      this.currentId = newCurrentId;
      this.currentTab = newCurrentTab;
      this.setSliderCss();
    }
  }

  setSliderCss() {
    let width = 0;
    let left = 0;
    if (this.currentTab) {
      width = this.currentTab.css("width");
      left = this.currentTab.offset().left;
    }
    $(".nav-tab-slider").css("width", width);
    $(".nav-tab-slider").css("left", left);
  }
}

new NavigationPage();
